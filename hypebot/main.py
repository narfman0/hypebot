import socket
import time

import twitter
from pytimeparse import parse as parse_time

from hypebot import log, settings


LOGGER = log.create_logger(__name__)


def create_twitter_api():
    return twitter.Api(
        consumer_key=settings.TWITTER_CONSUMER_KEY,
        consumer_secret=settings.TWITTER_CONSUMER_SECRET,
        access_token_key=settings.TWITTER_ACCESS_TOKEN,
        access_token_secret=settings.TWITTER_ACCESS_SECRET,
    )


def update(s, twitter, last_split_index):
    """ Update loop. Returns current world index. """
    s.send(b"getsplitindex\r\n")
    current_split_index = int(s.recv(1024))
    if last_split_index != current_split_index:
        logger.info(f"Split index changed to {current_split_index}")
    if last_split_index == 6 and current_split_index == 7:
        s.send(b"getdelta\r\n")
        # odd unicode prepended here: \xe2\x88\x923, appended \r\n
        delta = s.recv(1024)[3:].decode("utf-8").strip()
        logger.info(f"Split delta: {delta}")
        delta = parse_time(delta)
        if delta < 0:
            twitter.PostUpdate(f"narfman0 on p.b. pace with delta {delta}")
    return current_split_index


def main():
    twitter = create_twitter_api()
    last_split_index = -1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((settings.LIVESPLIT_HOST, settings.LIVESPLIT_PORT))
    while True:
        try:
            last_split_index = update(s, twitter, last_split_index)
        except socket.error as e:
            if e.errno == errno.ECONNRESET:
                logger.info("Socket connection reset, attempting to reconnect")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((settings.LIVESPLIT_HOST, settings.LIVESPLIT_PORT))
        time.sleep(1)


if __name__ == "__main__":
    main()
