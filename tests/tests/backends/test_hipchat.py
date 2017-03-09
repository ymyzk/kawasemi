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

from kawasemi.backends.hipchat import HipChatChannel
from kawasemi.exceptions import HttpError, ImproperlyConfigured


config = settings.CHANNELS["CHANNELS"]["hipchat"]


class HipChatChannelTestCase(TestCase):
    def setUp(self):
        self.channel = HipChatChannel(**config)

    def test_init(self):
        with self.assertRaises(TypeError):
            HipChatChannel(**{})

        with self.assertRaises(ImproperlyConfigured):
            conf = deepcopy(config)
            conf["color"] = "blue"
            HipChatChannel(**conf)

        with self.assertRaises(ImproperlyConfigured):
            conf = deepcopy(config)
            conf["notify"] = "true"
            HipChatChannel(**conf)

    @mock.patch("requests.post")
    def test_send(self, m):
        response = requests.Response()
        response.status_code = requests.codes.no_content
        m.return_value = response

        self.channel.send("Test message")

        self.channel.send("Test message with `color=green`.\n"
                          "https://www.hipchat.com/",
                          options={"hipchat": {"color": "green"}})

        self.channel.send("Test message with `message_format=text`.\n"
                          "https://www.hipchat.com/",
                          options={"hipchat": {"message_format": "text"}})

    @mock.patch("requests.post")
    def test_send_fail_invalid_token(self, m):
        response = requests.Response()
        response.status_code = requests.codes.bad_request
        m.return_value = response

        with self.assertRaises(HttpError):
            self.channel.send("Test message", fail_silently=False)

        self.channel.send("Test message", fail_silently=True)
