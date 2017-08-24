# coding: utf-8

"""setup details for the application"""

from setuptools import setup

setup(
    name="exch",
    version='0.1',
    description='A CLI app to see currency exchange rates.',
    url='https://github.com/anshulc95/exch',
    author='Anshul Chauhan',
    author_email='anshulchauhan@outlook.com',
    license='MIT',
    py_modeules=['exch'],
    install_requires=[
        'Click>=6.7',
        'requests==2.18.2',
    ],
    entry_points='''
        [console_scripts]
        exch=exch.core:cli
    ''',
)
