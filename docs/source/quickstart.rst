Quickstart
==========

Installation
------------

* Install kawasemi with your favorite package manager:

  .. code-block:: shell

     pip install kawasemi

* Add ``'kawasemi'`` to your ``INSTALLED_APPS`` setting:

  .. code-block:: python

     INSTALLED_APPS = [
         # Other apps
         'kawasemi',
     ]

* Add ``KAWASEMI`` to your project settings. You must obtain API keys or tokens from each service.

  * If you want to send notifications to HipChat:

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

  * You can use one or more channels. To send notifications to both HipChat and Slack:

    .. code-block:: python

       KAWASEMI = {
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

       KAWASEMI = {
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

   import kawasemi

   kawasemi.send("Sample notification.")
