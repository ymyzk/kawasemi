# -*- coding: utf-8 -*-
from __future__ import unicode_literals
try:
    from unittest import mock
except ImportError:
    import mock

from django.conf import settings
from django.test import TestCase
import requests

from kawasemi.backends.twitter import TwitterChannel
from kawasemi.exceptions import HttpError


config = settings.CHANNELS["CHANNELS"]["twitter"]


class TwitterChannelTestCase(TestCase):
    def setUp(self):
        self.channel = TwitterChannel(**config)

    @mock.patch("requests.post")
    def test_send(self, m):
        response = requests.Response()
        response.status_code = requests.codes.ok
        m.return_value = response

        self.channel.send("First tweet!")

    @mock.patch("requests.post")
    def test_send_fail_invalid_token(self, m):
        response = requests.Response()
        response.status_code = requests.codes.unauthorized
        m.return_value = response

        with self.assertRaises(HttpError):
            self.channel.send("Test tweet", fail_silently=False)

        self.channel.send("Test tweet", fail_silently=True)
