# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod

from six import add_metaclass


@add_metaclass(ABCMeta)
class BaseChannel(object):
    @abstractmethod
    def send(self, message, fail_silently=False, options=None):
        pass
