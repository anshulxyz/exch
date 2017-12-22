# **`exch`**

![travis CI stability badge](https://travis-ci.org/anshulc95/exch.svg?branch=master)
![python version supported badge](https://img.shields.io/pypi/pyversions/exch.svg)
![code coverage percentage of the current build badge](https://codecov.io/gh/anshulc95/exch/branch/master/graph/badge.svg)
[![PyPI version of the app badge](https://img.shields.io/pypi/v/exch.svg)](https://pypi.python.org/pypi/exch)

An application to see the currency exchange rates right from your command-line.

### Features:
* offline support
* default curreny
* list the available currencies

## Installation
```
$ pip install exch
```

## basic usage

```
$ exch -a 99 -b USD -t INR
99.0 USD = 6372.61 INR

$ exch --amount 199 --base EUR --target JPY
199.0 EUR = 25613.29 JPY
```

## Demo

[![asciicast](https://asciinema.org/a/153885.png)](https://asciinema.org/a/153885)


## Commands
|Short|Long|Description|Example|
|---|---|---|---|
|`-t`|`--target`|Currency you're converting to.|`exch -t INR`|
|`-b`|`--base`|Currency you're converting from.|`exch -b EUR`|
|`-a`|`--amount`|Amount of money to convert|`exch -a 99`|
|`-st`|`--set_target`|Set the new tagert currency|`exch -t CAD -st`|
|`-sb`|`--set_base`|Set the new tagert currency|`exch -b USD -sb`|
||`--help`|Show help message.|`exch --help`|
|`currencies`||List the Currencies that are available.|`exch currencies`|
|`sync`||Get the latest exchange rates for local use|`exch sync`|

## Advance usage

### Default amount is 1

```
$ exch -b USD -t PHP
1.0 USD = 51.23 PHP
```

### Default currencies

When no base or target given, the program assumes the default currencies.
```
$ exch
1.0 USD = 64.02 INR
```

Set the currency in use as default with `-sb` for base and `-st` for target.
```
$ exch -a 99 -b EUR -t NZD -sb -st
99.0 EUR = 168.00 NZD

$ exch
1.0 EUR = 1.70 NZD
```

## Built with

Programming language
* [Python3](https://www.python.org/)

Libraries used:
* [Click](http://click.pocoo.org/6/) - for making the command-line interface
* [Requests](http://docs.python-requests.org/en/master/) - for API calls

## Contribution

For contribution, please refer [CONTRIBUTING.md](CONTRIBUTING.md)

## Changlog

For changelog, please refer [CHANGELOG.md](CHANGELOG.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)
file for details
