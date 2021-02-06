from kocrawl.dust import DustCrawler
from unittest import TestCase


class DustTest(TestCase):

    def test(self):
        crawler = DustCrawler()
        output = crawler.request_debug("서을", "오늘")
        self.assertIsInstance(output, tuple)
