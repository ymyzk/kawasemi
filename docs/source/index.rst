kawasemi
========

.. image:: kawasemi.png
   :alt: Kawasemi's logo

**kawasemi** is a Python library for sending notifications.

Kawasemi provides the following features:

* Very simple ways to send notification

  * GitHub, HipChat, Slack, Twitter, and Yo are supported

* Integrations with web application frameworks helps to load configurations

  * Django is supported

At a Glance
-----------
After installation and configuration, you can send notifications with a following simple code:

.. code-block:: python

   # Python
   from kawasemi import Kawasemi
   kawasemi = Kawasemi(config)
   kawasemi.send("Sample notification.")

   # In Django application
   from kawasemi.django import send
   send("Sample notification.")

See `Quickstart`_ page for more details.

Contents
--------
.. toctree::
   :maxdepth: 2

   quickstart
   send
   cli
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
.. _Quickstart: https://kawasemi.readthedocs.io/en/latest/quickstart.html
