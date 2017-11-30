""" unit testing the helper functions """

import pkg_resources
from exch.helpers import fixer

FIXER_RATES_JSON_TEST = pkg_resources.resource_filename('exch', 'data/fixer_rates.json')


def test_fixer_same_currency_code():
    """ when the same currency is base as well as target """
    assert fixer('USD', 'USD', 1, FIXER_RATES_JSON_TEST) == 1.00
    assert fixer('INR', 'INR', 1, FIXER_RATES_JSON_TEST) == 1.00

def test_fixer_usd_to_inr():
    """ fixer_io base: USD, target: INR """
    assert fixer('USD', 'INR', 1, FIXER_RATES_JSON_TEST) > 60

def test_fixer_usd_to_jpy():
    """ fixer_io base: USD, target: JPY """
    assert fixer('USD', 'JPY', 1, FIXER_RATES_JSON_TEST) > 90

def test_fixer_gbp_to_php_value_99():
    """ fixer_io base: GBP, target: PHP, value: 99 """
    assert fixer('GBP', 'PHP', 99, FIXER_RATES_JSON_TEST) > 50

def test_fixer_eur_to_aud_value_99():
    assert fixer('EUR', 'AUD', 99, FIXER_RATES_JSON_TEST) > 1.2 * 99

def test_fixer_nzd_to_eur_value():
    """ checking since stored values are in terms of EUR as base """
    assert fixer('NZD', 'EUR', 1, FIXER_RATES_JSON_TEST) > 0.5

def test_fixer_invalid_currency():
    """ when invalid currency is passed to fixer.io """
    assert fixer('USD', 'TTT', 1, FIXER_RATES_JSON_TEST) == "KeyError: Invalid curreny"
