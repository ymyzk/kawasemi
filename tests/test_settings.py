from os import environ


SECRET_KEY = "fake-secret-key"

INSTALLED_APPS = [
    "tests",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

MIDDLEWARE_CLASSES = []

CHANNELS = {
    "CHANNELS": {
        "hipchat": {
            "_backend": "kawasemi.backends.hipchat.HipChatChannel",
            # Required
            "api_id": "api_id",
            "token": "token",
            # Optional
            "base_url": "base_url",
            "color": "red",
            "notify": True
        },
        "slack": {
            "_backend": "kawasemi.backends.slack.SlackChannel",
            # Required
            "url": "url",
            # Optional
            "username": "username",
            "icon_emoji": ":smile:",
            "channel": "channel"
        },
        "twitter": {
            "_backend": "kawasemi.backends.twitter.TwitterChannel",
            # Required
            "api_key": "api_key",
            "api_secret": "api_secret",
            "access_token": "access_token",
            "access_token_secret": "access_token_secret"
        },
        "yo": {
            "_backend": "kawasemi.backends.yo.YoChannel",
            # Required
            "api_token": "api_token",
            # Optional
            "username": "username"
        }
    }
}
