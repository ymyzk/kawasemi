# -*- coding: utf-8 -*-
from copy import deepcopy

import pytest
import requests

from kawasemi.backends.slack import SlackChannel
from kawasemi.exceptions import HttpError, ImproperlyConfigured


config = {
    "_backend": "kawasemi.backends.slack.SlackChannel",
    "url": "url"
}


@pytest.fixture()
def channel():
    return SlackChannel(**config)


class TestSlackChannel(object):
    def test_init(self):
        with pytest.raises(ImproperlyConfigured):
            conf = deepcopy(config)
            conf["icon_emoji"] = ":+1:"
            conf["icon_url"] = "http://www.example.com/"
            SlackChannel(**conf)

    def test_send(self, channel, mocker):
        post = mocker.patch("requests.post")
        response = requests.Response()
        response.status_code = requests.codes.ok
        post.return_value = response

        channel.send("Test message.\nhttps://slack.com/")

        channel.send("Test message. `unfurl_links=True`\n"
                          "https://slack.com/",
                          options={"slack": {"unfurl_links": True}})

        channel.send("Test message with attachments", options={
            "slack": {
                "attachments": [
                    {
                        "fallback": "Attachment 1",
                        "text": "Attachment 1",
                        "color": "#36a64f"
                    },
                    {
                        "fallback": "Attachment 2",
                        "text": "Attachment 2",
                        "color": "warning",
                        "fields": [
                            {
                                "title": "Field 1",
                                "value": "Field 1 value",
                                "short": False
                            },
                            {
                                "title": "Field 2",
                                "value": "Field 2 value",
                                "short": True
                            },
                            {
                                "title": "Field 3",
                                "value": "Field 3 value",
                                "short": True
                            }
                        ]
                    }
                ]
            }
        })

    def test_send_fail_invalid_url(self, channel, mocker):
        post = mocker.patch("requests.post")
        response = requests.Response()
        response.status_code = requests.codes.forbidden
        post.return_value = response

        with pytest.raises(HttpError):
            channel.send("Test message", fail_silently=False)

        channel.send("Test message", fail_silently=True)
