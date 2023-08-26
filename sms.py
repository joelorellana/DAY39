from twilio.rest import Client


class SMS(object):

    def __init__(self):
        self.account_sid = 'ACf60c47d2ec3f6205616461ebc3b05024'
        self.auth_token = 'd9c4f12ef0ccffbc72051b415095281a'
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
