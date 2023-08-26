import requests


class Sheet:
    def __init__(self, sheet="https://api.sheety.co/933220403ff9a29d1549da128febf048/flightDeals/prices"):
        self.headers = {
            'Authorization': 'Bearer secret'
        }
        self.sheet = sheet

    def read_sheet(self):
        response = requests.get(self.sheet, headers=self.headers, verify=False)
        text = response.json()['prices']
        return text

    def write_sheet(self, row_id, key, msg):
        """
        Writes a message to a specific row in the sheet.

        Args:
            row_id (int): The ID of the row to write the message to.
            key (str): The key to use in the JSON object.
            msg (str): The message to write.

        Returns:
            None
        """
        json = {
            "price": {
                key: msg
            }
                }
        put_url = self.sheet + f"/{row_id}"
        send = requests.put(put_url, headers=self.headers, json=json, verify=False)
        print(send.text)
