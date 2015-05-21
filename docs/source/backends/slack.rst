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
               "URL": "https://hooks.slack.com/services/ABCDEF/GHIJKLM/1234567890",
               # Optional
               "USERNAME": "django-channels",
               # You can set either ICON_URL or ICON_EMOJI
               "ICON_URL": "https://slack.com/img/icons/app-57.png",
               "ICON_EMOJI": ":ghost:",
               # Ex. 1 "CHANNEL": "#general"
               # Ex. 2 "CHANNEL": "@username"
               "CHANNEL": "#general"
           }
       }
   }

.. _Slack: https://slack.com/
.. _Incoming WebHooks: https://api.slack.com/incoming-webhooks
.. _Slack API: https://api.slack.com/
.. _this page: https://my.slack.com/services/new/incoming-webhook
