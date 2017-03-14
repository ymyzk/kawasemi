# -*- coding: utf-8 -*-
import pytest

from kawasemi.backends.base import BaseChannel


class TestBaseChannel(object):
    def test_init(self):
        with pytest.raises(TypeError):
            BaseChannel()

    def test_set_payload_from_options(self):
        payload = {}
        options = {
            "test": {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3"
            }
        }
        payload_keys = ["key1", "key2"]

        BaseChannel._set_payload_from_options(
            payload, options, "test", payload_keys)

        assert len(payload) == len(payload_keys)
        for key in payload:
            assert key in payload_keys
            assert payload[key] == options["test"][key]
