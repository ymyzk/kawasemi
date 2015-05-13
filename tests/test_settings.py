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
        "channels.backends.hipchat.HipChatChannel": {
            # Required
            "API_ID": environ.get("CHANNELS_HIPCHAT_API_ID"),
            "TOKEN": environ.get("CHANNELS_HIPCHAT_TOKEN"),
            # Optional
            "BASE_URL": environ.get("CHANNELS_HIPCHAT_BASE_URL", None)
        },
        "channels.backends.slack.SlackChannel": {
            # Required
            "URL": environ.get("CHANNELS_SLACK_URL"),
            # Optional
            "USERNAME": environ.get("CHANNELS_SLACK_USERNAME", None),
            "ICON_URL": environ.get("CHANNELS_SLACK_ICON_URL", None),
            "ICON_EMOJI": environ.get("CHANNELS_SLACK_ICON_EMOJI", None),
            "CHANNEL": environ.get("CHANNELS_SLACK_CHANNEL", None)
        }
    }
}
