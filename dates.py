import datetime


def get_today():
    """
    Get the current date in the format of day/month/year.

    :return: A string representing the current date.
    """
    return datetime.date.today().strftime("%d/%m/%Y")


def get_tomorrow():
    """
    Returns: a date in format dd/mm/yyyy
    """
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return tomorrow.strftime("%d/%m/%Y")


def get_six_months_later():
    """
    Returns: a date in format dd/mm/yyyy
    """
    six_months_later = datetime.date.today() + datetime.timedelta(days=180)
    return six_months_later.strftime("%d/%m/%Y")


print(get_today())
print(get_tomorrow())
print(get_six_months_later())
