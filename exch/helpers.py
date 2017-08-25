""" helper functions to gather the currency rates """

from urllib.parse import urlencode
import requests

def fixer(base, target, value, date='latest'):
    """get currency exchange rate from fixer.io in JSON"""

    main_api = 'http://api.fixer.io/{}?'.format(date)
    url = main_api + urlencode({'base':base})

    try:
        json_data = requests.get(url).json()
        result = round(json_data['rates'][target] * value, 2)
    except requests.exceptions.ConnectionError:
        result = "Connection Error"
    except KeyError:
        result = 1.00 if (base == target) else "Invalid currency"

    return result

#def google_finance_converter(base, target, value):
#    """ parse the Google Finance Converter html to extract the value"""
#    pass
