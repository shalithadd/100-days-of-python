import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
title_lst = [title_tag.get_text() for title_tag in (soup.select('div h3.title'))]
title_lst.reverse()

with open('movies.text', 'w', encoding='utf-8') as f:
    for title in title_lst:
        f.write(f'{title}\n')

