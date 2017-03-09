# -*- coding: utf-8 -*-
from copy import deepcopy

import pytest
import requests

from kawasemi.backends.hipchat import HipChatChannel
from kawasemi.exceptions import HttpError, ImproperlyConfigured


config =  {
    "_backend": "kawasemi.backends.hipchat.HipChatChannel",
    # Required
    "api_id": "api_id",
    "token": "token"
}


@pytest.fixture()
def channel():
    return HipChatChannel(**config)


class TestHipChatChannel(object):
    def test_init(self):
        with pytest.raises(TypeError):
            HipChatChannel(**{})

        with pytest.raises(ImproperlyConfigured):
            conf = deepcopy(config)
            conf["color"] = "blue"
            HipChatChannel(**conf)

        with pytest.raises(ImproperlyConfigured):
            conf = deepcopy(config)
            conf["notify"] = "true"
            HipChatChannel(**conf)

    def test_send(self, channel, mocker):
        post = mocker.patch("requests.post")
        response = requests.Response()
        response.status_code = requests.codes.no_content
        post.return_value = response

        channel.send("Test message")

        channel.send("Test message with `color=green`.\n"
                     "https://www.hipchat.com/",
                     options={"hipchat": {"color": "green"}})

        channel.send("Test message with `message_format=text`.\n"
                     "https://www.hipchat.com/",
                     options={"hipchat": {"message_format": "text"}})

    def test_send_fail_invalid_token(self, channel, mocker):
        post = mocker.patch("requests.post")
        response = requests.Response()
        response.status_code = requests.codes.bad_request
        post.return_value = response

        with pytest.raises(HttpError):
            channel.send("Test message", fail_silently=False)

        channel.send("Test message", fail_silently=True)
