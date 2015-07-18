Twitter
=======
`Twitter`_ is an online social networking service that enables users to send and read short 140-character messages called "tweets".

django-channels uses `one`_ of the `REST APIs`_ for sending tweets.

Settings
--------
You can obtain keys and access tokens from `Twitter Application Management`_.

.. code-block:: python

   CHANNELS = {
       "CHANNELS": {
           "channels.backends.twitter.TwitterChannel": {
                # Required
                # Consumer Key (API Key)
                "api_key": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                # Consumer Secret (API Secret)
                "api_secret": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                # Access Token
                "access_token": "0123456789-ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                # Access Token Secret
                "access_token_secret": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
           }
       }
   }

Options
-------
You can specify all parameters available in the `API`_. For instance:

.. code-block:: python

   import channels

   channels.send("Sample tweet with location.", options={
       "twitter": {
           "lat": 37.7821120598956,
           "long": -122.400612831116
       }
   })

.. _Twitter: https://twitter.com
.. _one: https://dev.twitter.com/rest/reference/post/statuses/update
.. _API: https://dev.twitter.com/rest/reference/post/statuses/update
.. _REST APIs: https://dev.twitter.com/rest/public
.. _Twitter Application Management: https://apps.twitter.com
