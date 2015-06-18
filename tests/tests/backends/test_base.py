# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from channels.backends.base import BaseChannel


class BaseChannelTestCase(TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            BaseChannel()
