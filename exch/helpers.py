""" helper functions to gather the currency rates """

from urllib.parse import urlencode
import requests
from decimal import Decimal, getcontext

getcontext().prec = 2

def fixer(base, target, value=1, date='latest'):
    """get currency exchange rate from fixer.io in JSON"""
    
    main_api = 'http://api.fixer.io/{}?'.format(date)
    url = main_api + urlencode({'base':base})
    json_data = requests.get(url).json()

    return round(json_data['rates'][target] * value, 2)

def google_finance_converter(base, target, value):
    """ parse the Google Finance Converter html to extract the value"""
    pass
