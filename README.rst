``exch``
========

.. image:: https://travis-ci.org/anshulc95/exch.svg?branch=master
    :target: https://travis-ci.org/anshulc95/exch

A commandline application built using python to see foreign exchange
rates andcurrency conversion.

It parses exchange rates from the following service(s):

   `fixer.io`_

Prerequisites:
--------------

-  `Python 3`_
-  `pip3`_
-  `git`_

Installation:
-------------

::

    $ git clone https://github.com/anshulc95/exch.git
    $ cd exch
    $ pip install --editable . -r requirements.txt  

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

+---------+-----------+-------------------------------------------+-------------------+
| Short   | Long      | Description                               | Example           |
+=========+===========+===========================================+===================+
| -t      | –target   | Currency you are converting from.         |  ``exch -t EUR``  |
+---------+-----------+-------------------------------------------+-------------------+
| -b      | –base     | Currency you're converting to.            |  ``exch -b INR``  |
+---------+-----------+-------------------------------------------+-------------------+
| -a      | –amount   | The amount of base currency to convert.   |  ``exch -a 99``   |
+---------+-----------+-------------------------------------------+-------------------+
| -h      | –help     | Displays the help text.                   |  ``exch --help``  |
+---------+-----------+-------------------------------------------+-------------------+

Development setup
-----------------

Use ``virtualenv`` for development in an isolated Python environment.

Install the testing dependecies:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ pwd
    /home/username/somedir/exch
    $ virtualenv venv -p python3
    $ source venv/bin/activate
    (venv) $ pip install --editable . -r requirements.txt -r test-requirements.txt

Running the tests
~~~~~~~~~~~~~~~~~

::

    (venv) $ pytest

To generate the test coverage:

::

    (venv) $ pytest --cov=exch --cov-report=term

Built With
----------

-  `Click`_ - a Python package for creating beautiful command line
   interfaces
-  `requests`_ - HTTP library for Python

Contributing
------------

1. Fork it (https://github.com/anshulc95/exch/fork)
2. Create your feature branch (``git checkout -b feature/fooBar``)
3. Commit your changes (``git commit -am 'Add some fooBar'``)
4. Push to the branch (``git push origin feature/fooBar``)
5. Create a new Pull Request

License
-------

This project is licensed under the MIT License - see the `LICENSE.md`_
file for details

.. _fixer.io: http://fixer.io/
.. _Python 3: https://www.python.org/download/releases/3.5.2/
.. _pip3: https://pypi.python.org/pypi/pip
.. _git: https://git-scm.com
.. _Click: http://click.pocoo.org/6/
.. _requests: http://docs.python-requests.org/en/master/
.. _LICENSE.md: LICENSE.md
