""" test the click and terminal behaviour """

import json
import pytest
import pkg_resources
from click.testing import CliRunner
from exch.cli import cli

FILEPATH = pkg_resources.resource_filename('exch', 'data/defaults.json')


@pytest.fixture
def runner():
    """ prefix alias function """
    return CliRunner()

def test_click_same_currency_code():
    """ test terminal behaviour for same currency code """
    result = runner().invoke(cli, ['-t', 'USD', '-b', 'USD'])
    assert result.exit_code == 0
    assert result.output == '1.0 USD = 1.0 USD\n'

def test_invalid_base_currency_code():
    result = runner().invoke(cli, ['-t', 'USD', '-b', 'AAA'])
    assert result.exit_code == 0
    assert result.output == "KeyError: Invalid curreny\n"

def test_invalid_target_currency_code():
    result = runner().invoke(cli, ['-t', 'OOO'])
    assert result.exit_code == 0
    assert result.output == "KeyError: Invalid curreny\n"

def test_invalid_amount_value():
    result = runner().invoke(cli, ['-a', 'TT'])
    assert result.exit_code == 2

def test_setting_default_base():
    result = runner().invoke(cli, ['-b', 'CAD', '-sb'])
    assert result.exit_code == 0
    # not testing the output because that depends upon the current exchange rate
    with open(FILEPATH) as json_file:
        json_data = json.load(json_file)
    assert json_data['base'] == 'CAD'

def test_setting_default_target():
    result = runner().invoke(cli, ['-t', 'NZD', '-st'])
    assert result.exit_code == 0
    with open(FILEPATH) as json_file:
        json_data = json.load(json_file)
    assert json_data['target'] == 'NZD'
