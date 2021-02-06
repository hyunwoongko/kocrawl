from unittest import TestCase
from kocrawl.daum_news import DaumNewsCrawler


class DaumDictTest(TestCase):

    def test(self):
        crawler = DaumNewsCrawler()
        output = crawler.request_debug(3)
        self.assertIsInstance(output, tuple)
