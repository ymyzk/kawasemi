Quickstart
==========

Requirements
------------

Python
^^^^^^
* Python 2.7+
* Python 3.5+
* PyPy
* PyPy3

Supported Frameworks
^^^^^^^^^^^^^^^^^^^^
* Django 1.11
* Django 2.0
* Django 2.1
* Django 2.2

Installation
------------
Install kawasemi with your favorite package manager:

.. code-block:: shell

   pip install kawasemi

Note: Please use the latest version of setuptools, pip, and wheel.

.. code-block:: shell

   pip install -U setuptools pip wheel

Configurations
--------------
You can write the configuration of kawasemi with a dictionary object.

* If you want to send notifications to HipChat:

  .. code-block:: python

     config = {
         "CHANNELS": {
             "hipchat": {
                 "_backend": "kawasemi.backends.hipchat.HipChatChannel",
                 "api_id": "1234567",
                 "token": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
             }
         }
     }

* You can use one or more channels. To send notifications to both HipChat and Slack:

  .. code-block:: python

     config = {
         "CHANNELS": {
             "hipchat": {
                "_backend": "kawasemi.backends.hipchat.HipChatChannel",
                 "api_id": "1234567",
                 "token": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
             },
             "slack": {
                 "_backend": "kawasemi.backends.slack.SlackChannel",
                 "url": "https://hooks.slack.com/services/ABCDEF/GHIJKLM/1234567890"
             }
         }
     }

* Of course, you can send a message to two different rooms simultaneously.
  To send notifications to two different HipChat rooms:

  .. code-block:: python

     config = {
         "CHANNELS": {
             "hipchat_first": {
                "_backend": "kawasemi.backends.hipchat.HipChatChannel",
                 "api_id": "1234567",
                 "token": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
             },
             "hipchat_second": {
                "_backend": "kawasemi.backends.hipchat.HipChatChannel",
                 "api_id": "3456789",
                 "token": "abcdefghijklmnopqrstuvwxyz0987654321"
             }
         }
     }


Usage
-----
You can send notifications with a following simple code:

.. code-block:: python

   from kawasemi import Kawasemi

   config = {
       "CHANNELS": {
           "hipchat": {
               "_backend": "kawasemi.backends.hipchat.HipChatChannel",
               "api_id": "1234567",
               "token": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
           }
       }
   }
   kawasemi = Kawasemi(config)
   kawasemi.send("Sample notification.")
   kawasemi.send("Another notification.")


Integration with Django
^^^^^^^^^^^^^^^^^^^^^^^
You can load configurations of kawasemi from ``settings.py`` by using this integration.

1. Add ``'kawasemi'`` to your ``INSTALLED_APPS`` setting:

  .. code-block:: python

     INSTALLED_APPS = [
         # Other apps
         'kawasemi.django',
     ]

2. Add ``KAWASEMI`` to your project settings. You must obtain API keys or tokens from each service.

  .. code-block:: python

     KAWASEMI = {
         "CHANNELS": {
             "hipchat": {
                 "_backend": "kawasemi.backends.hipchat.HipChatChannel",
                 "api_id": "1234567",
                 "token": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
             }
         }
     }

3. You can send notifications with a following simple code:

.. code-block:: python

   from kawasemi.django import send

   send("Sample notification.")
