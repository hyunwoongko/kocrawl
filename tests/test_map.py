from kocrawl.map import MapCrawler
from unittest import TestCase


class MapTest(TestCase):

    def test(self):
        crawler = MapCrawler()
        output = crawler.request_debug("서울", "영화관")
        self.assertIsInstance(output, tuple)
