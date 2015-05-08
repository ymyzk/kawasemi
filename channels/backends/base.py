# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod

from six import add_metaclass

from channels.exceptions import ImproperlyConfigured


@add_metaclass(ABCMeta)
class BaseChannel(object):
    @abstractmethod
    def send(self, message):
        pass

    def load_required_config(self, config, key_attrs):
        for key, attr in key_attrs.items():
            value = config.get(key, None)
            if value is None:
                raise ImproperlyConfigured("Required configuration: " + key)
            setattr(self, attr, value)

    def load_optional_config(self, config, key_attrs):
        for key, attr in key_attrs.items():
            value = config.get(key, None)
            if value is not None:
                setattr(self, attr, value)
