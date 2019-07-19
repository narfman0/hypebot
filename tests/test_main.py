from unittest import TestCase
from unittest.mock import patch

from hypebot import main


class TestHypebot(TestCase):
    @patch("hypebot.main.twitter")
    def test_create_twitter_api(self, twitter):
        main.create_twitter_api()
