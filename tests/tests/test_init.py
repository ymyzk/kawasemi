# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase
try:
    from unittest import mock
except ImportError:
    import mock

import kawasemi


class ChannelsModuleTestCase(TestCase):
    def test_load_module(self):
        import kawasemi.backends.slack
        module_name = "kawasemi.backends.slack"
        module = kawasemi._load_module(module_name)
        self.assertEqual(module, kawasemi.backends.slack)

    def test_load_backend(self):
        from kawasemi.backends.slack import SlackChannel
        klass_name = "kawasemi.backends.slack.SlackChannel"
        klass = kawasemi._load_backend(klass_name)
        self.assertEqual(klass, SlackChannel)

    def test__send_channel_not_exist(self):
        settings = {
            "CHANNELS": {}
        }

        with self.assertRaises(Exception):
            kawasemi._send("message", settings, channel_name="not_exists",
                           fail_silently=False, options=None)

    @mock.patch("kawasemi._load_backend")
    def test__send_all_channels(self, m):
        """test case for channel_name=None

        :type m: mock.MagicMock
        """
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

        kawasemi._send("message", settings, channel_name=None,
                       fail_silently=False, options=None)
        self.assertEqual(m.call_count, len(settings["CHANNELS"]))
        m.assert_any_call(settings["CHANNELS"]["channel1"]["_backend"])
        m.assert_any_call(settings["CHANNELS"]["channel2"]["_backend"])

    @mock.patch("kawasemi._load_backend")
    def test__send_specific_channel(self, m):
        """test case for channel_name != None

        :type m: mock.MagicMock
        """
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

        kawasemi._send("message", settings, channel_name="channel1",
                       fail_silently=False, options=None)
        m.assert_called_once_with(settings["CHANNELS"]["channel1"]["_backend"])
