# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from kawasemi.backends.base import BaseChannel


class BaseChannelTestCase(TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            BaseChannel()

    def test_set_payload_from_options(self):
        payload = {}
        options = {
            "test": {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3"
            }
        }
        payload_keys = ["key1", "key2"]

        BaseChannel._set_payload_from_options(
            payload, options, "test", payload_keys)

        self.assertEqual(len(payload), len(payload_keys))
        for key in payload:
            self.assertTrue(key in payload_keys)
            self.assertEqual(payload[key], options["test"][key])
