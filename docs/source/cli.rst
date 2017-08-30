CLI (Beta)
==========
You can use kawasemi as a command line application.
Currently, kawasemi CLI is in beta.

Configuration
-------------
Write configuration for kawasemi CLI in a JSON file called ``.kawasemirc``:

.. code-block:: javascript

   {
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

Running
-------
Run ``kawasemi`` command:

.. code-block:: shell

   kawasemi "Hello world!!"

Run ``kawasemi --help`` for more details.
