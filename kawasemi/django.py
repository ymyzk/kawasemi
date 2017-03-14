# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from kawasemi import Kawasemi


def _load_django_settings():
    from django.conf import settings
    return settings.KAWASEMI


_sender = Kawasemi(_load_django_settings())
send = _sender.send
