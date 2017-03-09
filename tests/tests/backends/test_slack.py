# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from copy import deepcopy
try:
    from unittest import mock
except ImportError:
    import mock

from django.conf import settings
from django.test import TestCase
import requests

from kawasemi.backends.slack import SlackChannel
from kawasemi.exceptions import HttpError, ImproperlyConfigured


config = settings.CHANNELS["CHANNELS"]["slack"]


class SlackChannelTestCase(TestCase):
    def setUp(self):
        self.channel = SlackChannel(**config)

    def test_init(self):
        with self.assertRaises(ImproperlyConfigured):
            conf = deepcopy(config)
            conf["icon_emoji"] = ":+1:"
            conf["icon_url"] = "http://www.example.com/"
            SlackChannel(**conf)

    @mock.patch("requests.post")
    def test_send(self, m):
        response = requests.Response()
        response.status_code = requests.codes.ok
        m.return_value = response

        self.channel.send("Test message.\nhttps://slack.com/")

        self.channel.send("Test message. `unfurl_links=True`\n"
                          "https://slack.com/",
                          options={"slack": {"unfurl_links": True}})

        self.channel.send("Test message with attachments", options={
            "slack": {
                "attachments": [
                    {
                        "fallback": "Attachment 1",
                        "text": "Attachment 1",
                        "color": "#36a64f"
                    },
                    {
                        "fallback": "Attachment 2",
                        "text": "Attachment 2",
                        "color": "warning",
                        "fields": [
                            {
                                "title": "Field 1",
                                "value": "Field 1 value",
                                "short": False
                            },
                            {
                                "title": "Field 2",
                                "value": "Field 2 value",
                                "short": True
                            },
                            {
                                "title": "Field 3",
                                "value": "Field 3 value",
                                "short": True
                            }
                        ]
                    }
                ]
            }
        })

    @mock.patch("requests.post")
    def test_send_fail_invalid_url(self, m):
        response = requests.Response()
        response.status_code = requests.codes.forbidden
        m.return_value = response

        with self.assertRaises(HttpError):
            self.channel.send("Test message", fail_silently=False)

        self.channel.send("Test message", fail_silently=True)
