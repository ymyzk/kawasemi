Yo
==
`Yo`_ is the simplest and most efficient communication tool in the world.

django-channels uses one of the `API`_ for sending Yos.

Settings
--------
You can obtain an API token from `Yo Dashboard`_.

.. code-block:: python

   CHANNELS = {
       "CHANNELS": {
           "yo": {
               "_backend": "channels.backends.yo.YoChannel",
               # Required
               # Your API token
               "api_token": environ.get("CHANNELS_YO_API_TOKEN"),
               # Optional
               # The recipient's username
               "username": environ.get("CHANNELS_YO_USERNAME"),
           }
       }
   }

Text
----
You can send Yo with text (30 characters max) with Yo API v2.0.

.. code-block:: python

   import channels

   # Yo with text
   self.channel.send("text")


Options
-------
You can send Yo Location or Yo Link by specifying options. For example:

.. code-block:: python

   import channels

   # Yo Link
   self.channel.send(None, options={
       "yo": {
           "link": "http://docs.justyo.co/v1.0/docs/yo"
       }
   })

   # Yo Location
   self.channel.send(None, options={
       "yo": {
           "location": "35.0261581,135.7818476"
       }
   })

Please note that you can only send link or location, but not both.

.. _Yo: https://www.justyo.co
.. _API: http://docs.justyo.co/v2.0/docs/yo
.. _Yo Dashboard: https://dev.justyo.co
