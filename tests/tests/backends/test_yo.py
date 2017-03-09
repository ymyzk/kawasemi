# -*- coding: utf-8 -*-
from __future__ import unicode_literals
try:
    from unittest import mock
except ImportError:
    import mock

from django.conf import settings
from django.test import TestCase
import requests

from kawasemi.backends.yo import YoChannel
from kawasemi.exceptions import HttpError


config = settings.CHANNELS["CHANNELS"]["yo"]


class YoChannelTestCase(TestCase):
    def setUp(self):
        self.channel = YoChannel(**config)

    @mock.patch("requests.post")
    def test_send(self, m):
        response = requests.Response()
        response.status_code = requests.codes.ok
        m.return_value = response

        # Just Yo
        self.channel.send(None)

        # Yo with text
        self.channel.send("🍣")

        # Yo Link
        self.channel.send(None, options={
            "yo": {"link": "http://docs.justyo.co/v1.0/docs/yo"}})

        # Yo Location
        self.channel.send(None, options={
            "yo": {"location": "35.0261581,135.7818476"}})

    @mock.patch("requests.post")
    def test_send_fail(self, m):
        response = requests.Response()
        response.status_code = requests.codes.forbidden
        m.return_value = response

        with self.assertRaises(HttpError):
            self.channel.send(None, fail_silently=False)

        self.channel.send(None, fail_silently=True)
