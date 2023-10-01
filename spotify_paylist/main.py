import os
from dotenv import load_dotenv
from spotipy import Spotify, SpotifyOAuth
import requests
from bs4 import BeautifulSoup


load_dotenv('.env')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')


URL = 'https://www.billboard.com/charts/hot-100/'
date = input('What year would you like to travel? (YYYY-MM-DD): ')

# Get top 100 songs from Billboard.com for the given date
response = requests.get(url=f'{URL}{date}')
soup = BeautifulSoup(response.text, 'html.parser')
# Select song titles
songs_lst = [(title.get_text()).strip() for title in (soup.select('li h3.c-title'))]

# Authenticate spotify
scope = "playlist-modify-private"
sp = Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=scope,
        show_dialog=True,
        cache_path='token.txt',
        username=os.getenv('SP_USERNAME')
    )
)
user_id = sp.current_user()['id']
year = date.split('-')[0]

track_uri_lst = []

for song in songs_lst:
    result = sp.search(q=f'track:{song} year:{year}', type='track')
    try:
        # Get track uri and append to track_uri_lst
        track_uri_lst.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print(f'No track found for {song}, skipped.')

# Create new playlist for date
playlist = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False)
playlist_id = playlist['id']

# Add tracks to playlist
sp.playlist_add_items(playlist_id=playlist_id, items=track_uri_lst)
