#!/usr/bin/env python3

""""
exch
=====

A CLI application built using python to see currency exchange rates.

:copyright: (c) 2017 by Anshul Chauhan
"""

import json
import click
import pkg_resources
from exch.helpers import fixer, fixer_sync
from exch.file_handling import get_default_base, get_default_target,\
                               set_default_base, set_default_target

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

RATES_FIXER_JSON_FILE = pkg_resources.resource_filename('exch', 'data/fixer_rates.json')
DEFAULT_JSON_FILE = pkg_resources.resource_filename('exch', 'data/defaults.json')

@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--base', '-b', default=get_default_base(DEFAULT_JSON_FILE),
              type=str, show_default=True,
              help='Currency you are converting from.')
@click.option('--target', '-t', default=get_default_target(DEFAULT_JSON_FILE),
              type=str, show_default=True, help='Currency you\'re converting to.')
@click.option('--amount', '-a', default=1.0, type=float, show_default=True,
              help='Amount to convert.')
@click.option('--set_base', '-sb', is_flag=True, default=False,
              help='Set new default base.')
@click.option('--set_target', '-st', is_flag=True, default=False,
              help='Set new default target.')
def cli(ctx, base, target, amount, set_base, set_target):
    """
    Get the latetst currency exchange rates from:

    \b
        - fixer.io
    """

    if ctx.invoked_subcommand is None:
        output = fixer(base, target, amount, RATES_FIXER_JSON_FILE)
        if isinstance(output, float):
            # 2:.2f for two decimal values, manually specified
            output = "{0} {1} = {2:.2f} {3}".format(amount, base, output, target)

        if set_base:
            set_default_base(base, DEFAULT_JSON_FILE)

        if set_target:
            set_default_target(target, DEFAULT_JSON_FILE)

        click.echo(output)

# subcommands

@cli.command()
def currencies():
    """ prints the list of currencies available """
    with open(RATES_FIXER_JSON_FILE) as rates_json_file:
        json_rates = json.load(rates_json_file)
    list_of_currencies = []
    list_of_currencies.append(json_rates['base'])
    for key in json_rates['rates']:
        list_of_currencies.append(key)
    list_of_currencies.sort()
    click.echo(', '.join(list_of_currencies))

@cli.command()
def sync():
    """ download the latest rates """
    if fixer_sync(RATES_FIXER_JSON_FILE) in range(200, 300):
        click.echo("New rates have been saved.")
