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


def _load_django_settings():
    from django.conf import settings
    return settings.CHANNELS


def _send(message, settings, channel_name, fail_silently, options):
    if channel_name is None:
        channels = settings["CHANNELS"]
    else:
        try:
            channels = {"channel": settings["CHANNELS"][channel_name]}
        except KeyError:
            raise Exception("channels does not exist %s", channel_name)

    for _, config in channels.items():
        if "_backend" not in config:
            raise ImproperlyConfigured(
                "Specify the backend class in the channel configuration")

        channel = _load_backend(config["_backend"])(**config)
        channel.send(message, fail_silently=fail_silently, options=options)


def send(message, channel=None, fail_silently=False, options=None):
    """Send a notification to channels

    :param message: A message
    :type message: str | unicode
    :type fail_silently: bool
    :type options: dict
    """
    settings = _load_django_settings()
    _send(message, settings, channel, fail_silently, options)
