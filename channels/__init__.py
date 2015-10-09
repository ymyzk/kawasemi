# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import sys

from .exceptions import ImproperlyConfigured


_BACKENDS = {}


def _load_module(name):
    __import__(name)
    return sys.modules[name]


def _load_backend(name):
    try:
        return _BACKENDS[name]
    except KeyError:
        module_name, klass_name = name.rsplit(".", 1)
        module = _load_module(module_name)
        _BACKENDS[name] = getattr(module, klass_name)
        return _BACKENDS[name]


def send(message, fail_silently=False, options=None):
    """Send a notification to all configured backends

    :param message: A message
    :type message: str | unicode
    :type fail_silently: bool
    :type options: dict
    """
    from django.conf import settings

    for _, config in settings.CHANNELS["CHANNELS"].items():
        if "_backend" not in config:
            raise ImproperlyConfigured(
                "Specify the backend class in the channel configuration")

        channel = _load_backend(config["_backend"])(**config)
        channel.send(message, fail_silently=fail_silently, options=options)
