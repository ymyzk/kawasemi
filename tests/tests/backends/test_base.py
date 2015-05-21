# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from channels.backends.base import BaseChannel
from channels.exceptions import ImproperlyConfigured


class BaseChannelTestCase(TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            BaseChannel()


class TestChannel(BaseChannel):
    def send(self, message):
        pass


class TestChannelTestCase(TestCase):
    def test_load_required_config(self):
        channel = TestChannel()
        config = {
            "URL": "http://example.com",
            "USERNAME": "testuser"
        }
        channel.load_required_config(config, {
            "URL": "url"
        })
        self.assertEqual(channel.url, config["URL"])

        with self.assertRaises(ImproperlyConfigured):
            channel.load_required_config({}, {
                "URL": "url",
                "USERNAME": "username"
            })

    def test_load_optional_config(self):
        channel = TestChannel()
        config = {
            "URL": "http://example.com",
            "USERNAME": "testuser"
        }
        channel.load_optional_config(config, {
            "USERNAME": "username",
            "CHANNEL": "channel"
        })
        self.assertEqual(channel.username, config["USERNAME"])
        self.assertFalse(hasattr(self, "channel"))
