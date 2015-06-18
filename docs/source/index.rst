django-channels
===============
django-channels is a Django library for sending notifications.
HipChat, Slack, and Yo are supported for now.

At a Glance
-----------
After installation and configuration, you can send notifications to HipChat, Slack or Yo with a following simple code:

.. code-block:: python

   import channels

   channels.send("Sample notification.")

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
