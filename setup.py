# coding: utf-8

"""setup details for the application"""

from os import path
from codecs import open
from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="exch",
    version='0.1rc1',
    description='A CLI app to see currency exchange rates.',
    long_description=LONG_DESCRIPTION,

    url='https://github.com/anshulc95/exch',

    author='Anshul Chauhan',
    author_email='anshulchauhan@outlook.com',

    license='MIT',

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Terminals",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    keywords='terminal currency utilities',

    py_modules=['exch'],
    install_requires=[
        'click',
        'requests',
    ],
    extras_require={
        'test':[
            'tox',
            'pytest'
        ]
    },
    packages=['exch'],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        exch=exch.cli:cli
    ''',
)
