Quickstart
==========

Requirements
------------

Python
^^^^^^
* Python 2.7+
* Python 3.2+
* PyPy
* PyPy3

Django
^^^^^^
* Django 1.7
* Django 1.8

Installation
------------

* Install django-channels with your favorite package manager:

  .. code-block:: shell

     pip install django-channels

* Add ``'channels'`` to your ``INSTALLED_APPS`` setting:

  .. code-block:: python

     INSTALLED_APPS = [
         # Other apps
         'channels',
     ]

* Add ``CHANNELS`` to your project settings. You must obtain API keys or tokens from each service.

  * If you want to send notifications to HipChat:

    .. code-block:: python

       CHANNELS = {
           "CHANNELS": {
               "channels.backends.hipchat.HipChatChannel": {
                   "api_id": "1234567",
                   "token": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
               }
           }
       }

  * You can use one or more channels. To send notifications to both HipChat and Slack:

     .. code-block:: python

        CHANNELS = {
            "CHANNELS": {
                "channels.backends.hipchat.HipChatChannel": {
                    "api_id": "1234567",
                    "token": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
                },
                "channels.backends.slack.SlackChannel": {
                    "url": "https://hooks.slack.com/services/ABCDEF/GHIJKLM/1234567890"
                }
            }
        }

Usage
-----
You can send notifications with a following simple code:

.. code-block:: python

   import channels

   channels.send("Sample notification.")
