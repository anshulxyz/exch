# Contributing

1. Fork it (<https://github.com/anshulc95/exch/fork>)
2. Create your feature branch (`git checkout -b feature-issue_id-fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature-issue_id-fooBar`)
5. Create a new Pull Request

## Development setup

To install testing dependencies `cd` into you cloned fork and run `virtualenv`.

```
$ virtualenv -p python3 venv
$ source venv/bin/activate
(venv) $ pip install -e .[test]
```
and if you are using `zsh`
```
(venv) $ pip install -e .\[test\]
```
To run the tests:
```
(venv) $ tox
```
