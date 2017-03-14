# -*- coding: utf-8 -*-
import pytest

from kawasemi import Kawasemi


class TestKawasemi(object):
    def test_load_module(self):
        kawasemi = Kawasemi({})
        from kawasemi.backends import slack
        module_name = "kawasemi.backends.slack"
        assert kawasemi._load_module(module_name) == slack

    def test_load_backend(self):
        kawasemi = Kawasemi({})
        from kawasemi.backends.slack import SlackChannel
        klass_name = "kawasemi.backends.slack.SlackChannel"
        assert kawasemi._load_backend(klass_name) == SlackChannel

    def test_send_channel_not_exist(self):
        kawasemi = Kawasemi({
            "CHANNELS": {}
        })

        with pytest.raises(Exception):
            kawasemi.send("message", channel_name="not_exists",
                          fail_silently=False, options=None)

    # @mock.patch("kawasemi._load_backend")
    def test__send_all_channels(self, mocker):
        """test case for channel_name=None"""
        settings = {
            "CHANNELS": {
                "channel1": {
                    "_backend": "kawasemi.backends.hipchat.HipChatChannel",
                    "api_id": "api_id",
                    "token": "token"
                },
                "channel2": {
                    "_backend": "kawasemi.backends.slack.SlackChannel",
                    "url": "url"
                }
            }
        }
        kawasemi = Kawasemi(settings)
        lb = mocker.patch.object(kawasemi, "_load_backend")
        kawasemi.send("message", channel_name=None, fail_silently=False,
                      options=None)
        assert lb.call_count == len(settings["CHANNELS"])
        lb.assert_any_call(settings["CHANNELS"]["channel1"]["_backend"])
        lb.assert_any_call(settings["CHANNELS"]["channel2"]["_backend"])

    def test__send_specific_channel(self, mocker):
        """test case for channel_name != None"""
        settings = {
            "CHANNELS": {
                "channel1": {
                    "_backend": "kawasemi.backends.hipchat.HipChatChannel",
                    "api_id": "api_id",
                    "token": "token"
                },
                "channel2": {
                    "_backend": "kawasemi.backends.slack.SlackChannel",
                    "url": "url"
                }
            }
        }
        kawasemi = Kawasemi(settings)
        lb = mocker.patch.object(kawasemi, "_load_backend")
        kawasemi.send("message", channel_name="channel1", fail_silently=False,
                      options=None)
        lb.assert_called_once_with(
            settings["CHANNELS"]["channel1"]["_backend"])
