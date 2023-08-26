import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(override=True)
ACCOUNT_ID = os.getenv("TWILIO_ACCOUNT_ID")
AUTH_TOKEN = os.getenv("TWILIO_TOKEN_AUTH")


class SMS(object):

    def __init__(self):
        self.account_sid = ACCOUNT_ID
        self.auth_token = AUTH_TOKEN
        self.client = Client(self.account_sid, self.auth_token)

    def send_msg(self, number, message):
        """
        Sends a message to a given phone number.

        Args:
            number (str): The phone number to send the message to.
            message (str): The content of the message.

        Returns:
            None
        """
        message = self.client.messages.create(
            from_='+16189964125',
            body=message,
            to=number
        )
        print(message.sid)
