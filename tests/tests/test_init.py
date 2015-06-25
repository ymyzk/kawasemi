# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase

import channels


class ChannelsModuleTestCase(TestCase):
    def test_load_module(self):
        import channels.backends.slack
        name = "channels.backends.slack"
        module = channels._load_module(name)
        self.assertEqual(module, channels.backends.slack)

    def test_load_backend(self):
        from channels.backends.slack import SlackChannel
        name = "channels.backends.slack.SlackChannel"
        klass = channels._load_backend(name)
        self.assertEqual(klass, SlackChannel)
