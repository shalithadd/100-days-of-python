import json
import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv('../stock_trading_app/.env')

OWM_APIKEY = os.getenv('OWM_APIKEY')
OWM_Endpoint = 'https://api.openweathermap.org/data/3.0/onecall'
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('AUTH_TOKEN')
from_num = os.getenv('FROM_NUMBER')
to_num = os.getenv('TO_NUMBER')
LAT = '53.578461'
LONG = '-2.429840'


weather_params = {
    'lat': LAT,
    'lon': LONG,
    'appid': OWM_APIKEY,
    'units': 'metric',
    'exclude': 'current,minutely,daily',
}

response = requests.get(OWM_Endpoint, params=weather_params,)
response.raise_for_status()
data = response.json()

with open('weather_data.json', 'w') as f:
    json.dump(data, f, indent=4)

with open('weather_data.json', 'r') as f:
    data = json.load(f)

hourly_weather_data = data['hourly'][:12]
condition_codes = [x['weather'][0]['id'] for i, x in enumerate(hourly_weather_data)]

will_rain = False
for code in condition_codes:
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=from_num,
        to=to_num
    )
    print(message.status)

