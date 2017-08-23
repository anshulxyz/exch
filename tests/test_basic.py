""" unit testing the helper functions """

from exch.helpers import fixer

def test_fixer_same_currency_code():
    """ when the same currency is base as well as target """
    assert fixer('USD', 'USD', 1) == 1.00
    assert fixer('INR', 'INR', 1) == 1.00

def test_fixer_usd_to_inr():
    """ fixer_io base: USD, target: INR, on date 2017-05-12 """
    assert fixer('USD', 'INR', 1, date='2017-05-12') == round(64.307, 2)

def test_fixer_usd_to_jpy():
    """ fixer_io base: USD, target: JPY, on date 2017-05-12 """
    assert fixer('USD', 'JPY', 1, date='2017-05-12') == round(113.85, 2)

def test_fixer_gbp_to_php_value_99():
    """ fixer_io base: GBP, target: PHP, on date 2017-05-12, value: 99 """
    assert fixer('GBP', 'PHP', 99, date='2017-05-12') == round(63.942 * 99, 2)

def test_fixer_inavlid_currency():
    """ when invalid currency is passed to fixer.io """
    assert fixer('USD', 'TTT', 1) == "Invalid currency"
    assert fixer('HHRR', 'TTT', 1) == "Invalid currency"

# TODO: test for connection error
