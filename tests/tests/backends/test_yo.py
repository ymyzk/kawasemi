# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from copy import deepcopy

from django.conf import settings
from django.test import TestCase

from channels.backends.yo import YoChannel
from channels.exceptions import HttpError, ImproperlyConfigured


config = settings.CHANNELS["CHANNELS"]["channels.backends.yo.YoChannel"]


class YoChannelTestCase(TestCase):
    def setUp(self):
        self.channel = YoChannel(**config)

    def test_init(self):
        with self.assertRaises(TypeError):
            YoChannel(**{})

    def test_send(self):
        self.channel.send("Just Yo")

        self.channel.send("Yo Link", options={
            "yo": {"link": "http://docs.justyo.co/v1.0/docs/yo"}})

        self.channel.send("Yo Location", options={
            "yo": {"location": "35.0261581,135.7818476"}})

    def test_send_fail(self):
        conf = deepcopy(config)
        conf["api_token"] = "api_token"
        channel = YoChannel(**conf)

        with self.assertRaises(HttpError):
            channel.send("Yo", fail_silently=False)

        channel.send("Yo", fail_silently=True)
