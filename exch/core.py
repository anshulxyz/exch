#!/usr/bin/env python3

""""
exch
=====

A CLI application built using python to see currency exchange rates.

:copyright: (c) 2017 by Anshul Chauhan
"""

import click
from exch.helpers import fixer

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

__version__ = '0.1'

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--base', '-b', default='USD', type=str, show_default=True,
              help='Currency you are converting from.')
@click.option('--target', '-t', default='INR', type=str, show_default=True,
              help='Currency you\'re converting to.')
@click.option('--amount', '-a', default=1.0, type=float, show_default=True,
              help='Amount to convert.')
def cli(base, target, amount):
    """
    Get the latetst currency exchange rates from:

    \b
        - fixer.io
    """

    output = fixer(base, target, amount)
    click.echo(output)
