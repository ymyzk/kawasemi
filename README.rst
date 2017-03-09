kawasemi
========
.. image:: https://badge.fury.io/py/django-channels.svg
   :target: https://pypi.python.org/pypi/django-channels/
   :alt: PyPI version
.. image:: https://travis-ci.org/ymyzk/django-channels.svg?branch=master
   :target: https://travis-ci.org/ymyzk/django-channels
   :alt: Build Status
.. image:: https://readthedocs.org/projects/django-channels/badge/?version=latest
   :target: https://django-channels.readthedocs.io/
   :alt: Documentation Status
.. image:: https://codeclimate.com/github/ymyzk/django-channels/badges/gpa.svg
   :target: https://codeclimate.com/github/ymyzk/django-channels
   :alt: Code Climate
.. image:: https://coveralls.io/repos/ymyzk/django-channels/badge.svg?branch=master
   :target: https://coveralls.io/r/ymyzk/django-channels?branch=master
   :alt: Coverage Status
.. image:: https://requires.io/github/ymyzk/django-channels/requirements.svg?branch=master
   :target: https://requires.io/github/ymyzk/django-channels/requirements/?branch=master
   :alt: Requirements Status

**kawasemi** is a Django library for sending notifications.
HipChat, Slack, Twitter and Yo are supported for now.

**Note:** This project was named *django-channels*.
We renamed our project not to be confused with the official `Django Channels`_.

At a Glance
-----------
After installation and configuration, you can send notifications to HipChat,
Slack, Twitter, or Yo with a following simple code:

.. code-block:: python

   import kawasemi

   kawasemi.send("Sample notification.")

See `Quickstart`_ page for more details.

Requirements
------------

Python
^^^^^^
* Python 2.7+
* Python 3.3+
* PyPy
* PyPy3

Django
^^^^^^
* Django 1.8
* Django 1.9
* Django 1.10

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

.. _Documentation: https://django-channels.readthedocs.io/
.. _GitHub: https://github.com/ymyzk/django-channels
.. _Quickstart: https://django-channels.readthedocs.io/en/latest/quickstart.html
.. _Django Channels: https://channels.readthedocs.io/
