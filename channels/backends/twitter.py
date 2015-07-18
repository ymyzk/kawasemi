# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from requests_oauthlib import OAuth1

from .base import BaseChannel
from channels.exceptions import HttpError


class TwitterChannel(BaseChannel):
    url = "https://api.twitter.com/1.1/statuses/update.json"

    def __init__(self, api_key, api_secret, access_token, access_token_secret):
        """A channel for posting a tweet

        :type api_key: unicode | str
        :type api_secret: unicode | str
        :type access_token: unicode | str
        :type access_token_secret: unicode | str
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def send(self, message, fail_silently=False, options=None):
        payload = {
            "status": message
        }

        if options is not None and "twitter" in options:
            options = options["twitter"]
            if "in_reply_to_status_id" in options:
                payload["in_reply_to_status_id"] =\
                    options["in_reply_to_status_id"]
            if "possibly_sensitive" in options:
                payload["possibly_sensitive"] = options["possibly_sensitive"]
            if "lat" in options:
                payload["lat"] = options["lat"]
            if "long" in options:
                payload["long"] = options["long"]
            if "place_id" in options:
                payload["place_id"] = options["place_id"]
            if "display_coordinates" in options:
                payload["display_coordinates"] = options["display_coordinates"]
            if "trim_user" in options:
                payload["trim_user"] = options["trim_user"]
            if "media_ids" in options:
                payload["media_ids"] = options["media_ids"]

        auth = OAuth1(self.api_key, self.api_secret, self.access_token,
                      self.access_token_secret)

        try:
            response = requests.post(self.url, auth=auth, data=payload)
            if response.status_code != requests.codes.ok:
                raise HttpError(response.status_code, response.text)
        except:
            if not fail_silently:
                raise
