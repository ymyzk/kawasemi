# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

from django.conf import settings


CHANNELS = settings.CHANNELS["CHANNELS"]


def _load_module(name):
    __import__(name)
    return sys.modules[name]


def _load_backend(name):
    module_name, klass_name = name.rsplit(".", 1)
    module = _load_module(module_name)
    return getattr(module, klass_name)


def send(message, fail_silently=False):
    """Send a notification to all configured backends

    :param message: A message
    :type message: str | unicode
    :type fail_silently: bool
    """
    for klass, config in CHANNELS.items():
        channel = _load_backend(klass)(config)
        channel.send(message, fail_silently=fail_silently)
