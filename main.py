from sheety import Sheet
from sms import SMS
from tequila import Tequila
from dates import get_today, get_tomorrow, get_six_months_later


msg_sender = SMS()
my_sheet = Sheet()
my_tequila = Tequila()

content = my_sheet.read_sheet()  # first read sheet

for el in content:  # iterate through content to see if there are blank iata codes
    if el['iataCode'] == '':
        iata_code = my_tequila.get_iata_code(el['city'])
        el['iataCode'] = iata_code
        my_sheet.write_sheet(el['id'], 'iataCode', iata_code)
    else:
        continue
