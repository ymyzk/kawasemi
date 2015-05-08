# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from channels.backends.base import BaseChannel
from channels.exceptions import ImproperlyConfigured


class TestChannel(BaseChannel):
    def send(self, message):
        pass


class BaseChannelTestCase(TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            BaseChannel()

    def test_load_required_config(self):
        channel = TestChannel()
        config = {
            "URL": "http://example.com"
        }
        channel.load_required_config(config, {
            "URL": "url"
        })
        self.assertEqual(channel.url, config["URL"])

        with self.assertRaises(ImproperlyConfigured):
            channel.load_required_config({}, {
                "URL": "url"
            })
