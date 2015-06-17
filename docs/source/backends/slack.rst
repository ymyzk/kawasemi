Slack
=====
`Slack`_ is a platform for team communication.

django-channels uses `Incoming WebHooks`_ which is one of the `Slack API`_ for sending notifications.

Settings
--------
You can obtain a Webhook URL from `this page`_.

.. code-block:: python

   CHANNELS = {
       "CHANNELS": {
           "channels.backends.slack.SlackChannel": {
               # Required
               # Webhook URL
               "url": "https://hooks.slack.com/services/ABCDEF/GHIJKLM/1234567890",
               # Optional
               "username": "django-channels",
               # You can set either icon_url or icon_emoji
               "icon_url": "https://slack.com/img/icons/app-57.png",
               "icon_emoji": ":ghost:",
               # Ex. 1 "channel": "#general"
               # Ex. 2 "channel": "@username"
               "channel": "#general"
           }
       }
   }

.. _Slack: https://slack.com/
.. _Incoming WebHooks: https://api.slack.com/incoming-webhooks
.. _Slack API: https://api.slack.com/
.. _this page: https://my.slack.com/services/new/incoming-webhook
