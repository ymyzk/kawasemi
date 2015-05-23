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
            "BASE_URL": environ.get("CHANNELS_HIPCHAT_BASE_URL"),
            "COLOR": environ.get("CHANNELS_HIPCHAT_COLOR"),
            "NOTIFY": environ.get("CHANNELS_HIPCHAT_NOTIFY") == "True"
        },
        "channels.backends.slack.SlackChannel": {
            # Required
            "URL": environ.get("CHANNELS_SLACK_URL"),
            # Optional
            "USERNAME": environ.get("CHANNELS_SLACK_USERNAME"),
            "ICON_URL": environ.get("CHANNELS_SLACK_ICON_URL"),
            "ICON_EMOJI": environ.get("CHANNELS_SLACK_ICON_EMOJI"),
            "CHANNEL": environ.get("CHANNELS_SLACK_CHANNEL")
        }
    }
}
