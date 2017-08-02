# currency-convert-cli

## **`exch`**

A commandline application built using python to see foreign exchange rates and currency conversion.

It parses exchange rates from the following services:
* [fixer.io](http://fixer.io/)

## Installation:

```
$ git clone https://github.com/anshulc95/currency-convert-cli.git
$ cd currency-convert-cli
$ pip install --editable .
```

## Usage:

```
$ exch -v 99 -f USD -t INR
6345.801
$ exch --value 100 --curr_from EUR --curr_to CNY
793.71
```
Default value for currency exchange is 1.

```
$ exch -f USD -t PHP
50.379
```

| Short | Long | Description | Example |
|--------|--------|--------|--------|
| -t | --curr_to | This the currency you are trying to convert from | **`exch -t EUR`** |
| -f | --curr_from | This is the currency you\'re converting to. | **`exch -f INR`** |
| -v | --value | The amount you want to convert. | **`exch -v 99`** |
| | --help | Displays the help text. | **`exch --help`** |