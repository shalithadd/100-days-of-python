import os
from dotenv import load_dotenv
import requests

load_dotenv('.env')


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    sheet_endpoint = 'https://api.sheety.co/52d0e86a43ac5f22aa892f89acbb9d94/flightDeals/prices'
    token = os.getenv('SHEETY_TOKEN')
    headers = {'Authorization': token}

    def get_sheet_data(self):
        response = requests.get(url=self.sheet_endpoint, headers=self.headers)
        return response.json()["prices"]

    def update_iata_code(self, object_id, city_data):
        body = {'price': city_data}
        response = requests.put(url=f'{self.sheet_endpoint}/{object_id}', json=body, headers=self.headers)
        print(response.text)
