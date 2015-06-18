django-channels
===============
.. image:: https://badge.fury.io/py/django-channels.svg
   :target: https://pypi.python.org/pypi/django-channels/
   :alt: PyPI version
.. image:: https://travis-ci.org/ymyzk/django-channels.svg?branch=master
   :target: https://travis-ci.org/ymyzk/django-channels
   :alt: Build Status
.. image:: https://codeclimate.com/github/ymyzk/django-channels/badges/gpa.svg
   :target: https://codeclimate.com/github/ymyzk/django-channels
   :alt: Code Climate
.. image:: https://coveralls.io/repos/ymyzk/django-channels/badge.svg?branch=master
   :target: https://coveralls.io/r/ymyzk/django-channels?branch=master
   :alt: Coverage Status

django-channels is a Django library for sending notifications.
HipChat and Slack are supported for now.

At a Glance
-----------
After installation and configuration, you can send notifications to HipChat, Slack, or Yo with a following simple code:

.. code-block:: python

   import channels

   channels.send("Sample notification.")

Links
-----
* `Documentation`_
* `GitHub`_

.. _Documentation: http://django-channels.readthedocs.org/
.. _GitHub: https://github.com/ymyzk/django-channels
