# coding: utf-8

"""setup details for the application"""

from setuptools import setup

setup(
    name="ExchangeRates",
    version='0.1',
    description='The funniest joke in the world',
    url='https://github.com/anshulc95/exch',
    author='Anshul Chauhan',
    author_email='anshulchauhan@outlook.com',
    license='MIT',
    py_modeules=['exchange'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        exch=exchange:cli
    ''',
)
