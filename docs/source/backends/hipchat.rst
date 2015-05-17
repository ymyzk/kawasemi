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
               "API_ID": "1234567",
               # Room Notification Token
               "TOKEN": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
               # Optional
               # Only for HipChat Server
               "BASE_URL": "https://api.hipchat.com/v2/"
           }
       }
   }

.. _HipChat: https://www.hipchat.com/
.. _Room API: https://www.hipchat.com/docs/apiv2/method/send_room_notification
.. _HipChat Rooms Page: https://my.hipchat.com/rooms
