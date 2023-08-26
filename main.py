import os
from sheety import Sheet
from sms import SMS
from tequila import Tequila
from dates import get_tomorrow, get_six_months_later
from dotenv import load_dotenv

load_dotenv(override=True)

MY_NUMBER = os.getenv("MY_NUMBER")

# creating objects for project
msg_sender = SMS()
my_sheet = Sheet()
my_tequila = Tequila()

# READING FROM SHEET

content = my_sheet.read_sheet()  # first read sheet

for el in content:  # iterate through content to see if there are blank iata codes
    if el['iataCode'] == '':
        iata_code = my_tequila.get_iata_code(el['city'])
        el['iataCode'] = iata_code
        my_sheet.write_sheet(el['id'], 'iataCode', iata_code)
    else:
        continue

# CHECKING PRICES OF FLIGHTS
for el in content:
    iata = el['iataCode']
    saved_price = el['lowestPrice']
    tomorrow = get_tomorrow()
    six_months_later = get_six_months_later()
    actual_price = my_tequila.search_flights('LAX', iata, tomorrow, six_months_later)
    if actual_price is None:
        continue
    elif actual_price < saved_price:
        msg_sender.send_msg(MY_NUMBER, f"Lowest price found: ${actual_price}")
    else:
        print("No new price found", actual_price, saved_price)
