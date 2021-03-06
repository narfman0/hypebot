import os

TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.environ.get("TWITTER_ACCESS_SECRET")
LIVESPLIT_HOST = os.environ.get("LIVESPLIT_HOST", "localhost")
LIVESPLIT_PORT = int(os.environ.get("LIVESPLIT_PORT", "16834"))
