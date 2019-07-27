import errno
import socket
import time

import twitter

from hypebot import log, net, settings


LOGGER = log.create_logger(__name__)


def create_twitter_api():
    return twitter.Api(
        consumer_key=settings.TWITTER_CONSUMER_KEY,
        consumer_secret=settings.TWITTER_CONSUMER_SECRET,
        access_token_key=settings.TWITTER_ACCESS_TOKEN,
        access_token_secret=settings.TWITTER_ACCESS_SECRET,
    )


def update(livesplit_client, twitter, last_split_index):
    """ Update loop. Returns current world index. """
    current_split_index = int(livesplit_client.post("getsplitindex"))
    if last_split_index != current_split_index:
        LOGGER.info("Split index changed to %d", current_split_index)
    if last_split_index == 6 and current_split_index == 7:
        delta = livesplit_client.post("getdelta")
        pb_pace = "−" in delta
        LOGGER.info("Split delta: %s", delta)
        if pb_pace:
            twitter.PostUpdate(f"narfman0 on p.b. pace with delta {delta}")
    return current_split_index


def main():
    twitter = create_twitter_api()
    last_split_index = -1
    livesplit_client = net.LiveSplitClient()
    LOGGER.info("Connected and ready for updates...")
    while True:
        try:
            last_split_index = update(livesplit_client, twitter, last_split_index)
        except socket.error as e:
            if e.errno == errno.ECONNRESET:
                LOGGER.info("Socket connection reset, attempting to reconnect")
                livesplit_client.connect()
        time.sleep(1)


if __name__ == "__main__":
    main()
