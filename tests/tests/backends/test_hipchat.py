# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from copy import deepcopy

from django.conf import settings
from django.test import TestCase

from channels.backends.hipchat import HipChatChannel
from channels.exceptions import HttpError, ImproperlyConfigured


channels = settings.CHANNELS["CHANNELS"]
config = channels["channels.backends.hipchat.HipChatChannel"]


class HipChatChannelTestCase(TestCase):
    def setUp(self):
        self.channel = HipChatChannel(config)

    def test_init(self):
        with self.assertRaises(ImproperlyConfigured):
            HipChatChannel({})

        with self.assertRaises(ImproperlyConfigured):
            conf = deepcopy(config)
            conf["COLOR"] = "blue"
            HipChatChannel(conf)

        with self.assertRaises(ImproperlyConfigured):
            conf = deepcopy(config)
            conf["NOTIFY"] = "true"
            HipChatChannel(conf)

    def test_send(self):
        self.channel.send("Test message")

    def test_send_fail(self):
        conf = deepcopy(config)
        conf["TOKEN"] = "token"
        channel = HipChatChannel(conf)

        with self.assertRaises(HttpError):
            channel.send("Test message", fail_silently=False)

        channel.send("Test message", fail_silently=True)
