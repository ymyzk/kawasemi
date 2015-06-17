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
        self.channel.send("Test message")

    def test_send_fail(self):
        conf = deepcopy(config)
        conf["url"] = "https://hooks.slack.com/services/123/456/7890"
        channel = SlackChannel(**conf)

        with self.assertRaises(HttpError):
            channel.send("Test message", fail_silently=False)

        channel.send("Test message", fail_silently=True)
