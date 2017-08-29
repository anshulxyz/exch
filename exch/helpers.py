""" helper functions to gather the currency rates """

import requests

def fixer(base, target, value, date='latest'):
    """get currency exchange rate from fixer.io in JSON"""

    main_api = 'http://api.fixer.io/{}?'.format(date)
    url = requests.get(main_api, params={'base':base})

    try:
        json_data = requests.get(url.url).json()
        result = round(json_data['rates'][target] * value, 2)
    except requests.exceptions.ConnectionError:
        result = "Connection Error"
    except KeyError:
        result = 1.00 if base == target else "KeyError: Invalid curreny"

    return result

#def google_finance_converter(base, target, value):
#    """ parse the Google Finance Converter html to extract the value"""
#    pass
