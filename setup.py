# coding: utf-8

from setuptools import setup

setup (
    name="CurrencyConversionCli",
    version='0.1',
    py_modeules=['exchange'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        exch=exchange:cli
    ''',
)