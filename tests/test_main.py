from unittest import TestCase
from unittest.mock import MagicMock, patch

from hypebot import main


class TestHypebot(TestCase):
    @patch("hypebot.main.twitter")
    def test_create_twitter_api(self, twitter):
        main.create_twitter_api()

    def test_update_tweet(self):
        livesplit_client = MagicMock()
        livesplit_client.recv.side_effect = ["7", "\xe2\x88\x92-1:11"]
        twitter = MagicMock()
        main.update(livesplit_client, twitter, 6)
        self.assertTrue(twitter.PostUpdate.called)

    def test_update_no_tweet(self):
        livesplit_client = MagicMock()
        livesplit_client.recv.side_effect = ["7", "\xe2\x88\x9213"]
        twitter = MagicMock()
        main.update(livesplit_client, twitter, 6)
        self.assertFalse(twitter.PostUpdate.called)
