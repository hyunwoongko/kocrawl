from kocrawl.spell import SpellCrawler
from unittest import TestCase


class SpellTest(TestCase):

    def test(self):
        crawler = SpellCrawler()
        output = crawler.request_debug("서울 에서 밥을먹 었다.")
        self.assertIsInstance(output, tuple)
