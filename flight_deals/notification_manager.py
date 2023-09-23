import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv('.env')


class NotificationManager:
    def __init__(self):
        self.account_sid = os.getenv('TWILIO_SID')
        self.auth_token = os.getenv('TWILIO_TOKEN')
        self.from_number = os.getenv('FROM_NUMBER')
        self.to_number = os.getenv('TO_NUMBER')

    def send_message(self, data):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=data,
            from_=self.from_number,
            to=self.to_number
        )
        print(message.status)
