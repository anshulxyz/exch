""" module for the class for core of the application """

import pytest
from click.testing import CliRunner
from exch.core import cli
from exch.helpers import fixer, google_finance_converter

@pytest.fixture
def runner():
    return CliRunner()

def test_same_currency_code():
    """ when the same currency is base as well as target """
    result_usd = runner().invoke(cli, ['-f', 'USD', '-t', 'USD'])
    assert result_usd.exit_code == 0
    assert result_usd.output == "1.00\n"

    result_inr = runner().invoke(cli, ['-f', 'INR', '-t', 'INR'])
    assert result_inr.exit_code == 0
    assert result_inr.output == "1.00\n"

def test_fixer_usd_to_inr_():
    """ base: USD, target: INR, on the date of 2017-05-12 """
    assert fixer('USD', 'INR', date='2017-05-12') == round(64.307, 2)

def test_fixer_usd_to_jpy_():
    """ base: USD, target: JPY, on the date of 2017-05-12 """
    assert fixer('USD', 'JPY', date='2017-05-12') == round(113.85, 2)


#def test_fixer_inavlid_currency():
#    """ when invalid currency is passed to fixer.io """
#    pass

#def test_fixer_invalid_value_type():
#    """ when invalid value type is passed to fixer """
#    pass
