# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

import requests

from .base import BaseChannel
from channels.exceptions import HttpError, ImproperlyConfigured


class SlackChannel(BaseChannel):
    def __init__(self, url, username=None, channel=None, icon_emoji=None,
                 icon_url=None, **kwargs):
        self.url = url
        self.username = username
        self.channel = channel
        self.icon_emoji = icon_emoji
        self.icon_url = icon_url

        # Validation
        if self.icon_emoji is not None and self.icon_url is not None:
            raise ImproperlyConfigured(
                "Must not set both icon_emoji and icon_url")

    def send(self, message, fail_silently=False, options=None):
        payload = {
            "text": message
        }
        if self.channel is not None:
            payload["channel"] = self.channel
        if self.username is not None:
            payload["username"] = self.username
        if self.icon_emoji is not None:
            payload["icon_emoji"] = self.icon_emoji
        if self.icon_url is not None:
            payload["icon_url"] = self.icon_url
        if options is not None and "slack" in options:
            options = options["slack"]
            if "attachments" in options:
                payload["attachments"] = options["attachments"]
            if "unfurl_links" in options:
                payload["unfurl_links"] = options["unfurl_links"]
        data = {
            "payload": json.dumps(payload)
        }
        try:
            response = requests.post(self.url, data=data)
            if response.status_code != requests.codes.ok:
                raise HttpError(response.status_code, response.text)
        except:
            if not fail_silently:
                raise
