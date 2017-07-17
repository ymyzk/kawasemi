GitHub
======
`GitHub`_ is online source code hosting service for Git projects.

kawasemi uses one of the `REST API v3`_ for sending notification to GitHub.

Settings
--------
Please refer to `this page`_ on how to obtain a token.

.. code-block:: python

   config = {
       "CHANNELS": {
           "github": {
               "_backend": "kawasemi.backends.github.GitHubChannel",
               # Token
               "token": "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
               # Owner of the repository
               "owner": "ymyzk",
               # Repository
               "repository": "test-repo"
           }
       }
   }

Options
-------
You can specify all options available in the `REST API v3`_. For instance:

.. code-block:: python

   kawasemi.send("Issue Title", options={
       "github": {
           "body": """## ToDo
   - [ ] Introduce A
   - [ ] Refactor B""",
           "milestone": 123,
           "labels": ["enhancement"],
           "assignees": ["ymyzk"]
       }
   })

.. _GitHub: https://github.com
.. _REST API v3: https://developer.github.com/v3/issues/#create-an-issue
.. _this page: https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
