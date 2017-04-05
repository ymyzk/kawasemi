kawasemi
========
**kawasemi** is a Python library for sending notifications.
HipChat, Slack, Twitter and Yo are supported for now.

kawasemi can be used easily in your Python projects.
kawasemi also provides integration with web application frameworks which makes it
more easier to load configurations.

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

Contents
--------
.. toctree::
   :maxdepth: 2

   quickstart
   send
   backends/index
   license

Indices and tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Links
-----
* `Documentation`_
* `GitHub`_

.. _Documentation: https://kawasemi.readthedocs.io/
.. _GitHub: https://github.com/ymyzk/kawasemi
