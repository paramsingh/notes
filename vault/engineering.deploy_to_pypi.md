---
id: c7353bfb-dd2e-4b36-8463-70f26e9cc9dd
title: Deploy to PyPI
desc: ''
updated: 1642957308003
created: 1616188779688
---


Each package needs a `setup.py` file which pip will use to install the package.

Install the dependencies needed.

```
$ pip install --upgrade setuptools wheel twine
```

First, create the files that need to be uploaded.

```
$ python setup.py sdist bdist_wheel
```

This should create two files in the `dist` folder.

Create an account on https://pypi.org and a upload token.
Then, upload the file using twine. The username should be `__token__`
and password should be the token.

```
$ python3 -m twine upload dist/*
```
