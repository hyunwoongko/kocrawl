from kocrawl.weather import WeatherCrawler
from unittest import TestCase


class WeatherTest(TestCase):

    def test(self):
        crawler = WeatherCrawler()
        output = crawler.request_debug("서을", "이번주")
        self.assertIsInstance(output, tuple)

        output = crawler.request_debug("서을", "오늘")
        self.assertIsInstance(output, tuple)
