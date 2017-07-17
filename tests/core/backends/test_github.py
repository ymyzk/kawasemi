# -*- coding: utf-8 -*-
import pytest
import requests

from kawasemi.backends.github import GitHubChannel
from kawasemi.exceptions import HttpError, ImproperlyConfigured


config = {
    "_backend": "kawasemi.backends.github.GitHubChannel",
    "token": "token",
    "owner": "ymyzk",
    "repository": "kawasemi"
}


@pytest.fixture()
def channel():
    return GitHubChannel(**config)


class TestGitHubChannel(object):
    def test_send(self, channel, mocker):
        post = mocker.patch("requests.post")
        response = requests.Response()
        response.status_code = requests.codes.created
        post.return_value = response

        channel.send("My Issue Title")

        channel.send("Issue Title", options={
            "github": {
                "body": """## ToDo
- [ ] Introduce A
- [ ] Refactor B""",
                "labels": ["enhancement"],
                "assignees": ["ymyzk"]
            }
        })

    def test_send_fail_invalid_token(self, channel, mocker):
        post = mocker.patch("requests.post")
        response = requests.Response()
        response.status_code = requests.codes.unauthorized
        post.return_value = response

        with pytest.raises(HttpError):
            channel.send("Test title", fail_silently=False)

        channel.send("Test title", fail_silently=True)
