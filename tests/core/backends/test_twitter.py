# -*- coding: utf-8 -*-
import pytest
import requests

from kawasemi.backends.twitter import TwitterChannel
from kawasemi.exceptions import HttpError


@pytest.fixture()
def channel():
    config = {
        "_backend": "kawasemi.backends.twitter.TwitterChannel",
        "api_key": "api_key",
        "api_secret": "api_secret",
        "access_token": "access_token",
        "access_token_secret": "access_token_secret"
    }
    return TwitterChannel(**config)


class TestTwitterChannel(object):
    def test_send(self, channel, mocker):
        post = mocker.patch("requests.post")
        response = requests.Response()
        response.status_code = requests.codes.ok
        post.return_value = response

        channel.send("First tweet!")

    def test_send_fail_invalid_token(self, channel, mocker):
        post = mocker.patch("requests.post")
        response = requests.Response()
        response.status_code = requests.codes.unauthorized
        post.return_value = response

        with pytest.raises(HttpError):
            channel.send("Test tweet", fail_silently=False)

        channel.send("Test tweet", fail_silently=True)
