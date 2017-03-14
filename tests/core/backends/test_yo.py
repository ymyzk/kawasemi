# # -*- coding: utf-8 -*-
import pytest
import requests

from kawasemi.backends.yo import YoChannel
from kawasemi.exceptions import HttpError


@pytest.fixture()
def channel():
    config = {
        "_backend": "kawasemi.backends.yo.YoChannel",
        "api_token": "api_token",
    }
    return YoChannel(**config)


class TestYoChannel(object):
    def test_send(self, channel, mocker):
        post = mocker.patch("requests.post")
        response = requests.Response()
        response.status_code = requests.codes.ok
        post.return_value = response

        # Just Yo
        channel.send(None)

        # Yo with text
        channel.send(u"🍣")

        # Yo Link
        channel.send(None, options={
            "yo": {"link": "http://docs.justyo.co/v1.0/docs/yo"}})

        # Yo Location
        channel.send(None, options={
            "yo": {"location": "35.0261581,135.7818476"}})

    def test_send_fail(self, channel, mocker):
        post = mocker.patch("requests.post")
        response = requests.Response()
        response.status_code = requests.codes.forbidden
        post.return_value = response

        with pytest.raises(HttpError):
            channel.send(None, fail_silently=False)

        channel.send(None, fail_silently=True)
