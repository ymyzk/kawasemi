# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import sys
from typing import Dict, Optional, Text  # noqa: F401

from .backends.base import BaseChannel  # noqa: F401
from .exceptions import ImproperlyConfigured
from .types import SendOptions  # noqa: F401


_BACKENDS = {}  # type: Dict[str, BaseChannel]


def _load_module(name):
    # type: (str) -> BaseChannel
    __import__(name)
    return sys.modules[name]


def _load_backend(name):
    # type: (str) -> BaseChannel
    try:
        return _BACKENDS[name]
    except KeyError:
        module_name, klass_name = name.rsplit(".", 1)
        module = _load_module(str(module_name))
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
    # type: (Text, Optional[str], bool, Optional[SendOptions]) -> None
    """Send a notification to channels

    :param message: A message
    """
    settings = _load_django_settings()
    _send(message, settings, channel, fail_silently, options)
