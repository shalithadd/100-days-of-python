import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv('.env')


class FlightSearch:
    flight_location_endpoint = 'https://api.tequila.kiwi.com/locations/query'
    flight_search_endpoint = 'https://api.tequila.kiwi.com/v2/search'
    apikey = os.getenv('FLIGHT_SEARCH_APIKEY')
    headers = {'apikey': apikey, 'accept': 'application/json'}

    def get_iata_code(self, city):
        query = {'term': city, }
        response = requests.get(url=self.flight_location_endpoint, params=query, headers=self.headers)
        return response.json()

    def search_flight(self, departure_city, destination):
        date_from = datetime.now() + timedelta(days=1)
        to_date = (date_from + (timedelta(days=30) * 6)).strftime('%d/%m/%Y')

        query = {
            'fly_from': departure_city,
            'fly_to': destination,
            'date_from': date_from.strftime('%d/%m/%Y'),
            'date_to': to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            'curr': 'GBP',
        }

        response = requests.get(url=self.flight_search_endpoint, params=query, headers=self.headers)
        return response.json()

