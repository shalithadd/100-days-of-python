class FlightData:
    def __init__(self, data):
        self.departure_city = data['cityFrom']
        self.departure_airport_code = data['cityCodeFrom']
        self.destination_city = data['cityTo']
        self.destination_airport_code = data['cityCodeTo']
        self.price = data['price']
        self.fly_from = data['local_departure']
        self.fly_to = data['local_arrival']
