import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)

TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")


class Tequila:
    def __init__(self):
        self.url_location = "https://api.tequila.kiwi.com/locations/query"
        self.url_search = "https://api.tequila.kiwi.com/v2/search"

    def get_iata_code(self, city):
        """
        Retrieves the IATA code for a given city.

        Parameters:
            city (str): The name of the city for which the IATA code is to be retrieved.

        Returns:
            str: The IATA code corresponding to the given city.
        """
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "term": city
        }
        response = requests.get(self.url_location, headers=headers, params=params, verify=False)
        iata = response.json()["locations"][0]["code"]
        return iata

    def search_flights(self, origin, destination, from_date, to_date):
        """
        Searches for flights from an origin to a destination on a given date.
        """
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": from_date,
            "date_to": to_date,
            "one_per_date": 1,
            "one_for_city": 1
        }

        response = requests.get(self.url_search, headers=headers, params=params, verify=False)
        flights = response.json()["data"]
        if len(flights) == 0:
            return None
        else:
            price = flights[0]['price']
        return price

# prueba_tequila = Tequila()

# vuelos = prueba_tequila.search_flights(origin='PDX', destination='TYO', from_date=get_tomorrow(),
# to_date=get_six_months_later())
