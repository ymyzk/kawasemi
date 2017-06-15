kawasemi
========
.. image:: https://badge.fury.io/py/kawasemi.svg
   :target: https://pypi.python.org/pypi/kawasemi/
   :alt: PyPI version
.. image:: https://img.shields.io/pypi/pyversions/Django.svg
   :target: https://pypi.python.org/pypi/kawasemi/
   :alt: PyPI Python versions
.. image:: https://travis-ci.org/ymyzk/kawasemi.svg?branch=master
   :target: https://travis-ci.org/ymyzk/kawasemi
   :alt: Build Status
.. image:: https://readthedocs.org/projects/kawasemi/badge/?version=latest
   :target: https://kawasemi.readthedocs.io/
   :alt: Documentation Status
.. image:: https://codeclimate.com/github/ymyzk/kawasemi/badges/gpa.svg
   :target: https://codeclimate.com/github/ymyzk/kawasemi
   :alt: Code Climate
.. image:: https://coveralls.io/repos/ymyzk/kawasemi/badge.svg?branch=master
   :target: https://coveralls.io/r/ymyzk/kawasemi?branch=master
   :alt: Coverage Status
.. image:: https://requires.io/github/ymyzk/kawasemi/requirements.svg?branch=master
   :target: https://requires.io/github/ymyzk/kawasemi/requirements/?branch=master
   :alt: Requirements Status

.. image:: https://raw.githubusercontent.com/ymyzk/kawasemi/master/docs/source/kawasemi.png
   :alt: Kawasemi's logo

**kawasemi** is a Python library for sending notifications.
HipChat, Slack, Twitter and Yo are supported for now.

kawasemi can be used easily in your Python projects.
kawasemi also provides integration with web application frameworks which makes it
more easier to load configurations.

Note: This project was named *django-channels*.
We renamed our project not to be confused with the official `Django Channels`_.

At a Glance
-----------
After installation and configuration, you can send notifications to HipChat,
Slack, Twitter, or Yo with a following simple code:

.. code-block:: python

   # Python
   from kawasemi import Kawasemi
   kawasemi = Kawasemi(config)
   kawasemi.send("Sample notification.")

   # With Django
   from kawasemi.django import send
   send("Sample notification.")

See `Quickstart`_ page for more details.

Requirements
------------

Python
^^^^^^
* Python 2.7+
* Python 3.3+
* PyPy
* PyPy3

Supported Frameworks
^^^^^^^^^^^^^^^^^^^^
* Django 1.8
* Django 1.9
* Django 1.10
* Django 1.11

Installation
------------

.. code-block:: shell

   pip install kawasemi

Note: Please use the latest version of setuptools, pip, and wheel.

.. code-block:: shell

   pip install -U setuptools pip wheel


Links
-----
* `Documentation`_
* `GitHub`_

.. _Documentation: https://kawasemi.readthedocs.io/
.. _GitHub: https://github.com/ymyzk/kawasemi
.. _Quickstart: https://kawasemi.readthedocs.io/en/latest/quickstart.html
.. _Django Channels: https://channels.readthedocs.io/
