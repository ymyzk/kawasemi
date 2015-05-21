Sending Notification
====================

Simple Notification
-------------------
You can send a notification with a following code:

.. code-block:: python

   import channels

   channels.send("Sample notification.")

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

You can ignore errors with ``fail_silently`` argument:

.. code-block:: python

   import channels

   channels.send("Exceptions are ignored.", fail_silently=True)
