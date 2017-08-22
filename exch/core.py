#!/usr/bin/env python3

""""
exch
=====

A CLI application built using python to see currency exchange rates.

:copyright: (c) 2017 by Anshul Chauhan
"""

import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--base', '-f', default='USD', type=str,
              help='The currency you are trying to convert from.',
              show_default=True)
@click.option('--target', '-t', default='INR', type=str,
              help='The currency you\'re converting to.',
              show_default=True)
@click.option('--value', '-v', default=1, type=float,
              help='The amount you want to convert.',
              show_default=True)
def cli(base, target, value):
    """
    Get the latetst currency exchange rates.

    It gets exchange rates from:

    \b
        - fixer.io
    """
    if base == target:
        click.echo('1.00')
