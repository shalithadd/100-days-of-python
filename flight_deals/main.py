import json
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


DEPARTURE_CITY = 'LON'

data_manager = DataManager()

# with open('sheet_data', 'w') as f:
#     json.dump(data_manager.get_sheet_data(), f, indent=4)

with open('sheet_data', 'r') as f:
    sheet_data = json.load(f)

flight_search = FlightSearch()
low_price_alert = ''

for city in sheet_data:
    # if iata code is not in the sheet get iata code for tequila location api and update sheet data
    if not city['iataCode']:
        city['iataCode'] = flight_search.get_iata_code(city['city'])['locations'][0]['code']
        data_manager.update_iata_code(object_id=city['id'], city_data=city)

    # for each city in sheet data search cheap flights
    result = flight_search.search_flight(departure_city=DEPARTURE_CITY, destination=city['iataCode'])[
        'data'][0]

    min_price = city['lowestPrice']
    for i, v in enumerate(result):
        flight_data = FlightData(v)
        # Get only the first item from result list
        if i == 1:
            break
        # If price from result is lower than price in the sheet, create the message
        elif flight_data.price < min_price:
            message = (f'Low price alert! Only £{flight_data.price} to fly from {flight_data.departure_city}'
                       f'-{flight_data.departure_airport_code} to {flight_data.destination_city}-'
                       f'{flight_data.destination_airport_code}, form {flight_data.fly_from[:10]} to '
                       f'{flight_data.fly_to[:10]}.\n\n')
            low_price_alert += message

# Send the message
# notification_manager = NotificationManager()
# notification_manager.send_message(low_price_alert)

print(low_price_alert)