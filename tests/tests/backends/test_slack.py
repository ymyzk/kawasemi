# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from copy import deepcopy

from django.conf import settings
from django.test import TestCase

from channels.backends.slack import SlackChannel
from channels.exceptions import HttpError, ImproperlyConfigured


config = settings.CHANNELS["CHANNELS"]["channels.backends.slack.SlackChannel"]


class SlackChannelTestCase(TestCase):
    def setUp(self):
        self.channel = SlackChannel(**config)

    def test_init(self):
        with self.assertRaises(TypeError):
            SlackChannel(**{})

        with self.assertRaises(ImproperlyConfigured):
            conf = deepcopy(config)
            conf["icon_emoji"] = ":+1:"
            conf["icon_url"] = "http://www.example.com/"
            SlackChannel(**conf)

    def test_send(self):
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

    def test_send_fail(self):
        conf = deepcopy(config)
        conf["url"] = "https://hooks.slack.com/services/123/456/7890"
        channel = SlackChannel(**conf)

        with self.assertRaises(HttpError):
            channel.send("Test message", fail_silently=False)

        channel.send("Test message", fail_silently=True)
