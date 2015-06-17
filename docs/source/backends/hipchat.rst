HipChat
=======
`HipChat`_ is hosted group chat and video chat for companies and teams.

django-channels uses one of the `Room API`_ for sending notification to HipChat.

Settings
--------
You can obtain a Room API ID and a Room Notification Token from `HipChat Rooms Page`_.

.. code-block:: python

   CHANNELS = {
       "CHANNELS": {
           "channels.backends.hipchat.HipChatChannel": {
               # Required
               # Room API ID
               "api_id": "1234567",
               # Room Notification Token
               "token": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
               # Optional
               # Only for HipChat Server
               "base_url": "https://api.hipchat.com/v2/",
               # Background color for message
               # Valid values: yellow, green, red, purple, gray, random
               "color": "random"
               # Whether this message should trigger a user notification
               "notify": True
           }
       }
   }

.. _HipChat: https://www.hipchat.com/
.. _Room API: https://www.hipchat.com/docs/apiv2/method/send_room_notification
.. _HipChat Rooms Page: https://my.hipchat.com/rooms
