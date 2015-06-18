# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from .base import BaseChannel
from channels.exceptions import HttpError


class YoChannel(BaseChannel):
    url = "https://api.justyo.co/yo/"

    def __init__(self, api_token, username=None):
        self.api_token = api_token
        self.username = username

    def send(self, message, fail_silently=False, options=None):
        payload = {
            "api_token": self.api_token
        }

        if self.username is not None:
            payload["username"] = self.username

        if options is not None and "yo" in options:
            options = options["yo"]
            if "username" in options:
                payload["username"] = options["username"]
            if "link" in options:
                payload["link"] = options["link"]
            if "location" in options:
                payload["location"] = options["location"]

        try:
            response = requests.post(self.url, data=payload)
            if response.status_code != requests.codes.ok:
                raise HttpError(response.status_code, response.text)
        except:
            if not fail_silently:
                raise
