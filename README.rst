``exch``
========

.. image:: https://travis-ci.org/anshulc95/exch.svg?branch=master
    :target: https://travis-ci.org/anshulc95/exch
    
.. image:: https://img.shields.io/pypi/pyversions/exch.svg
    :target: https://github.com/anshulc95/exch

A commandline application built using python to see foreign exchange
rates andcurrency conversion.

It parses exchange rates from the following service(s):

   `fixer.io`_

Installation:
-------------

::

    $ pip install exch

Usage:
------

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

+----------+----------------+-------------------------------------------+-----------------------+
| Short    | Long           | Description                               | Example               |
+==========+================+===========================================+=======================+
| ``-t``   | ``--target``   | Currency you’re converting to.            |   ``exch -t EUR``     |
+----------+----------------+-------------------------------------------+-----------------------+
| ``-b``   | ``--base``     | Currency you are converting from.         |   ``exch -f INR``     |
+----------+----------------+-------------------------------------------+-----------------------+
| ``-a``   | ``--amount``   | The amount of base currency to convert.   |   ``exch -v 99``      |
+----------+----------------+-------------------------------------------+-----------------------+
| ``-h``   | ``--help``     | Displays the help text.                   |   ``exch --help``     |
+----------+----------------+-------------------------------------------+-----------------------+


Built With
----------

-  `Click`_ - a Python package for creating beautiful command line interfaces.
-  `requests`_ - HTTP library for Python

License
-------

This project is licensed under the MIT License - see the `LICENSE.md`_
file for details

.. _fixer.io: http://fixer.io/
.. _Click: http://click.pocoo.org/6/
.. _requests: http://docs.python-requests.org/en/master/
.. _LICENSE.md: LICENSE.md
