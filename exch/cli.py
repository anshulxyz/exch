#!/usr/bin/env python3

""""
exch
=====

A CLI application built using python to see currency exchange rates.

:copyright: (c) 2017 by Anshul Chauhan
"""

import click
from exch.helpers import fixer
from exch.file_handling import get_default_base, get_default_target, set_default_base, set_default_target

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

__version__ = '0.1'

DEFAULT_JSON_FILE = 'data/defaults.json'

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--base', '-b', default=get_default_base(DEFAULT_JSON_FILE), type=str, show_default=True,
              help='Currency you are converting from.')
@click.option('--target', '-t', default=get_default_target(DEFAULT_JSON_FILE), type=str, show_default=True,
              help='Currency you\'re converting to.')
@click.option('--amount', '-a', default=1.0, type=float, show_default=True,
              help='Amount to convert.')
@click.option('--set_base', '-sb', is_flag=True, default=False,
              help='Set new default base.')
@click.option('--set_target', '-st', is_flag=True, default=False,
              help='Set new default target.')
def cli(base, target, amount, set_base, set_target):
    """
    Get the latetst currency exchange rates from:

    \b
        - fixer.io
    """

    output = fixer(base, target, amount)
    # TODO: why am I using isinstance ?
    # why not use a different variable for storing amount
    if isinstance(output, float):
        output = "{} {} = {} {}".format(amount, base, output, target)

    if set_base:
        set_default_base(base, DEFAULT_JSON_FILE)

    if set_target:
        set_default_target(target, DEFAULT_JSON_FILE)

    click.echo(output)
