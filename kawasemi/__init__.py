# -*- coding: utf-8 -*-
from __future__ import absolute_import
from copy import deepcopy
import sys
from typing import Any, Dict, Optional, Text, TypeVar  # noqa: F401

from .__about__ import __version__
from .backends.base import BaseChannel
from .exceptions import ImproperlyConfigured
from .types import SendOptions  # noqa: F401

__all__ = ["Kawasemi", "__version__"]


C = TypeVar("C", bound=BaseChannel)


class Kawasemi(object):
    def __init__(self, settings):
        self.settings = settings
        self._backends = {}  # type: Dict[str, C]

    def _load_module(self, name):
        # type: (str) -> Any
        __import__(name)
        return sys.modules[name]

    def _load_backend(self, name):
        # type: (str) -> C
        try:
            return self._backends[name]
        except KeyError:
            module_name, klass_name = name.rsplit(".", 1)
            module = self._load_module(str(module_name))
            self._backends[name] = getattr(module, klass_name)
            return self._backends[name]

    def send(self, message, channel_name=None, fail_silently=False,
             options=None):
        # type: (Text, Optional[str], bool, Optional[SendOptions]) -> None
        """Send a notification to channels

        :param message: A message
        """
        if channel_name is None:
            channels = self.settings["CHANNELS"]
        else:
            try:
                channels = {
                    "__selected__": self.settings["CHANNELS"][channel_name]
                }
            except KeyError:
                raise Exception("channels does not exist %s", channel_name)

        for _, config in channels.items():
            if "_backend" not in config:
                raise ImproperlyConfigured(
                    "Specify the backend class in the channel configuration")

            backend = self._load_backend(config["_backend"])
            config = deepcopy(config)
            del config["_backend"]
            channel = backend(**config)
            channel.send(message, fail_silently=fail_silently, options=options)
