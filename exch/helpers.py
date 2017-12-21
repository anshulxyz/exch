""" helper functions to gather the currency rates """

import json
import requests

def fixer(base, target, value, file_path):
    """
    get currency exchange rate from fixer.io in JSON,
    take note that all the rates are stored as EUR as base
    """

    try:
        """
        try to find the json file which contains currency exchange rates
        """
        with open(file_path) as json_file:
            json_rates = json.load(json_file)
    except FileNotFoundError:
        """
        if file not found, 'fixer_sync' will download the latests rates,
        the range of 200-300 is for succesful HTTP code
        """
        if fixer_sync(file_path) in range(200, 300):
            with open(file_path) as json_file:
                json_rates = json.load(json_file)

    try:
        eur_to_target = json_rates['rates'][target]
        eur_to_base = json_rates['rates'][base]
        result = eur_to_target/eur_to_base * value
    except KeyError:
        if base == 'EUR':
            result = json_rates['rates'][target] * value
        elif target == 'EUR':
            result = (1.0/json_rates['rates'][base]) * value
        else:
            result = "KeyError: Invalid curreny"

    return result

def fixer_sync(file_path):
    """
    downloads the rates JSON to the local location,
    'file_path' is the location where the fixer.io rates will the placed,
    returns status_code, if it is 200 then file successfully created
    """
    url = 'http://api.fixer.io/latest'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as json_file:
            json_file.write(response.content)

    return response.status_code
