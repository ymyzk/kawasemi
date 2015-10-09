Sending Notification
====================

Simple Notification
-------------------
You can send a notification to all configured channels with a following code:

.. code-block:: python

   import channels

   channels.send("Sample notification.")

Options
-------
You can set some options for the each of backends:

.. code-block:: python

   import channels

   channels.send("Sample notification.", options={
       "hipchat": {
           "color": "green"
       },
       "slack": {
           "attachments": [
               {
                   "fallback": "Attachment 1",
                   "text": "Attachment 1",
                   "color": "#36a64f"
               }
           ]
       }
   })

Please refer to :doc:`backends/index` for all available options.

Exceptions
----------
You can handle errors by using ``try`` statement:

.. code-block:: python

   import channels

   try:
       channels.send("Sample notification.")
   except Exception as e:
       print("Error!!")
       print(e)

You can ignore errors with ``fail_silently`` parameter:

.. code-block:: python

   import channels

   channels.send("Exceptions are ignored.", fail_silently=True)

Send to a Specific Channel
--------------------------
By default, notifications are sent to all configured channels.
You can send notifications to a channel with ``channel`` parameter.

Example settings:

.. code-block:: python

   CHANNELS = {
       "CHANNELS": {
           "channel_1": {
               # ...
           },
           "channel_2": {
               # ...
           }
       }
   }

Send a notification to ``channel_1``:

.. code-block:: python

   channel.send("sample notification", channel="channel_1")
