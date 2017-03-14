# -*- coding: utf-8 -*-
from django.test import TestCase

import kawasemi.django


class DjangoModuleTestCase(TestCase):
    def test_load_django_settings(self):
        settings = kawasemi.django._load_django_settings()
        from .settings import KAWASEMI
        self.assertDictEqual(settings, KAWASEMI)
