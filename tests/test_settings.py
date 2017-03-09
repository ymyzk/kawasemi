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
            "api_id": environ.get("CHANNELS_HIPCHAT_API_ID"),
            "token": environ.get("CHANNELS_HIPCHAT_TOKEN"),
            # Optional
            "base_url": environ.get("CHANNELS_HIPCHAT_BASE_URL"),
            "color": environ.get("CHANNELS_HIPCHAT_COLOR"),
            "notify": environ.get("CHANNELS_HIPCHAT_NOTIFY") == "True"
        },
        "slack": {
            "_backend": "kawasemi.backends.slack.SlackChannel",
            # Required
            "url": environ.get("CHANNELS_SLACK_URL"),
            # Optional
            "username": environ.get("CHANNELS_SLACK_USERNAME"),
            "icon_url": environ.get("CHANNELS_SLACK_ICON_URL"),
            "icon_emoji": environ.get("CHANNELS_SLACK_ICON_EMOJI"),
            "channel": environ.get("CHANNELS_SLACK_CHANNEL")
        },
        "twitter": {
            "_backend": "kawasemi.backends.twitter.TwitterChannel",
            # Required
            "api_key": environ.get("CHANNELS_TWITTER_API_KEY"),
            "api_secret": environ.get("CHANNELS_TWITTER_API_SECRET"),
            "access_token": environ.get("CHANNELS_TWITTER_ACCESS_TOKEN"),
            "access_token_secret":
                environ.get("CHANNELS_TWITTER_ACCESS_TOKEN_SECRET")
        },
        "yo": {
            "_backend": "kawasemi.backends.yo.YoChannel",
            # Required
            "api_token": environ.get("CHANNELS_YO_API_TOKEN"),
            # Optional
            "username": environ.get("CHANNELS_YO_USERNAME")
        }
    }
}
