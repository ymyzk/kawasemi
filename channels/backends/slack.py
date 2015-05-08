# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

import requests

from .base import BaseChannel
from channels.exceptions import HttpError, ImproperlyConfigured


class SlackChannel(BaseChannel):
    def __init__(self, config):
        # Required
        self.load_required_config(config, {
            "URL": "url"
        })

        # Optional
        self.load_optional_config(config, {
            "USERNAME": "username",
            "CHANNEL": "channel",
            "ICON_EMOJI": "icon_emoji",
            "ICON_URL": "icon_url"
        })

        # Validation
        if hasattr(self, "icon_emoji") and hasattr(self, "icon_url"):
            raise ImproperlyConfigured(
                "Must not set both ICON_EMOJI and ICON_URL")

    def send(self, message, fail_silently=False):
        payload = {
            'text': message
        }
        if hasattr(self, "channel"):
            payload["channel"] = self.channel
        if hasattr(self, "username"):
            payload["username"] = self.username
        if hasattr(self, "icon_url"):
            payload["icon_url"] = self.icon_url
        if hasattr(self, "icon_emoji"):
            payload["icon_emoji"] = self.icon_emoji
        data = {
            'payload': json.dumps(payload)
        }
        try:
            response = requests.post(self.url, data=data)
            if response.status_code != 200:
                raise HttpError(response.status_code)
        except:
            if not fail_silently:
                raise
