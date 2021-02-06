from unittest import TestCase
from kocrawl.daum_dict import DaumDictCrawler


class DaumDictTest(TestCase):

    def test(self):
        crawler = DaumDictCrawler()
        output = crawler.request_debug(3)
        self.assertIsInstance(output, tuple)
