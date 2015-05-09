# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from copy import deepcopy
from django.conf import settings
from django.test import TestCase

from channels.backends.slack import SlackChannel
from channels.exceptions import ImproperlyConfigured


config = settings.CHANNELS["CHANNELS"]["channels.backends.slack.SlackChannel"]


class SlackChannelTestCase(TestCase):
    def setUp(self):
        self.channel = SlackChannel(config)

    def test_init(self):
        with self.assertRaises(ImproperlyConfigured):
            SlackChannel({})

        with self.assertRaises(ImproperlyConfigured):
            conf = deepcopy(config)
            conf["ICON_EMOJI"] = ":+1:"
            conf["ICON_URL"] = "http://www.example.com/"
            SlackChannel(conf)

    def test_send(self):
        self.channel.send("Test message")
