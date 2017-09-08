========
``exch``
========

.. image:: https://travis-ci.org/anshulc95/exch.svg?branch=master
    :target: https://travis-ci.org/anshulc95/exch

.. image:: https://img.shields.io/pypi/pyversions/exch.svg
    :target: https://github.com/anshulc95/exch

A command-line application built using python to see foreign exchange
rates and currency conversion.

It parses exchange rates from the following service(s):

   `fixer.io`_

Installation:
-------------

::

    $ pip install exch

Usage examples:
---------------

::

    $ exch -a 99 -b USD -t INR
    99.0 USD = 6343.92 INR

::

    $ exch --amount 199 --base EUR --target JPY
    199.0 EUR = 25613.29 JPY

Default amount for currency exchange is 1.

::

    $ exch -b USD -t PHP
    1.0 USD = 51.23 PHP

change default curreny
~~~~~~~~~~~~~~~~~~~~~~
::

    $ exch
    1.0 USD = 64.02 INR
    $ exch -b EUR -t NZD -sb
    1.0 EUR = 1.66 NZD
    $ exch
    1.0 EUR = 76.63 INR
    $ exch -b EUR -t CAD -st
    1.0 EUR = 1.46 CAD
    $ exch
    1.0 EUR = 1.46 CAD
    $ exch -b PHP -t JPY -sb -st
    1.0 PHP = 2.14 JPY
    $ exch
    1.0 PHP = 2.14 JPY

List of commands
~~~~~~~~~~~~~~~~
+-----------+--------------------+-------------------------------------------+-----------------------+
| Short     | Long               | Description                               | Example               |
+===========+====================+===========================================+=======================+
| ``-t``    | ``--target``       | Currency you’re converting to.            | ``exch -t INR``       |
+-----------+--------------------+-------------------------------------------+-----------------------+
| ``-b``    | ``--base``         | Currency you’re converting from.          | ``exch -b USD``       |
+-----------+--------------------+-------------------------------------------+-----------------------+
| ``-a``    | ``--amount``       | The amount of base currency to convert.   | ``exch -a 99``        |
+-----------+--------------------+-------------------------------------------+-----------------------+
| ``-st``   | ``--set_target``   | Set new default target currency.          | ``exch -t PHP -st``   |
+-----------+--------------------+-------------------------------------------+-----------------------+
| ``-sb``   | ``--set_base``     | Set new default base currency.            | ``exch -b EUR -sb``   |
+-----------+--------------------+-------------------------------------------+-----------------------+
| ``-h``    | ``--help``         | Displays the help text.                   | ``exch -h``           |
+-----------+--------------------+-------------------------------------------+-----------------------+

Built With
----------

-  `Click`_ - a Python package for creating beautiful command line interfaces.
-  `requests`_ - HTTP library for Python

License
-------

This project is licensed under the MIT License - see the `LICENSE.md`_
file for details

Contribution
------------
For contribution, please refer `CONTRIBUTING.md`_

.. _fixer.io: http://fixer.io/
.. _Click: http://click.pocoo.org/6/
.. _requests: http://docs.python-requests.org/en/master/
.. _LICENSE.md: LICENSE.md
.. _CONTRIBUTING.md: CONTRIBUTING.md