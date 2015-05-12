# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.test import TestCase

from channels.backends.hipchat import HipChatChannel
from channels.exceptions import ImproperlyConfigured


channels = settings.CHANNELS["CHANNELS"]
config = channels["channels.backends.hipchat.HipChatChannel"]


class HipChatChannelTestCase(TestCase):
    def setUp(self):
        self.channel = HipChatChannel(config)

    def test_init(self):
        with self.assertRaises(ImproperlyConfigured):
            HipChatChannel({})

    def test_send(self):
        self.channel.send("Test message")
