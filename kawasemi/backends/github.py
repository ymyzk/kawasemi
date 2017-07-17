# -*- coding: utf-8 -*-
import json

import requests

from .base import BaseChannel
from ..exceptions import HttpError


class GitHubChannel(BaseChannel):
    def __init__(self, token, owner, repository,
                 base_url="https://api.github.com", *args, **kwargs):
        self.token = token
        self.url = base_url + "/repos/" + owner + "/" + repository + "/issues"

    def send(self, message, fail_silently=False, options=None):
        headers = {
            "Authorization": "token " + self.token,
            "Content-Type": "application/json"
        }
        payload = {
            "title": message
        }

        self._set_payload_from_options(payload, options, "github", [
            "body", "milestone", "labels", "assignees"])

        try:
            response = requests.post(self.url,
                                     headers=headers,
                                     data=json.dumps(payload))
            if response.status_code != requests.codes.created:
                raise HttpError(response.status_code, response.text)
        except:
            if not fail_silently:
                raise
