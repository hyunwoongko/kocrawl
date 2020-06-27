"""
@auther Hyunwoong
@since {6/21/2020}
@see : https://github.com/gusdnd852
"""
from kocrawl.answerer.map_answerer import MapAnswerer
from kocrawl.base import BaseCrawler
from kocrawl.editor.map_editor import MapEditor
from kocrawl.searcher.map_searcher import MapSearcher


class MapCrawler(BaseCrawler):

    def __init__(self):
        self.searcher = MapSearcher()
        self.editor = MapEditor()
        self.answerer = MapAnswerer()

    def request(self, location: str, place: str) -> str:
        """
        지도를 크롤링합니다.
        (try-catch로 에러가 나지 않는 함수)

        :param location: 지역
        :param place: 장소
        :return: 해당지역 장소
        """

        try:
            return self.request_debug(location, place)
        except Exception:
            return self.answerer.sorry(
                "해당 지역은 알 수 없습니다."
            )

    def request_debug(self, location: str, place: str) -> str:
        """
        지도를 크롤링합니다.
        (에러가 나는 디버깅용 함수)

        :param location: 지역
        :param place: 장소
        :return: 해당지역 장소
        """

        result = self.searcher.search_naver_map(location, place)
        result = self.editor.edit_map(location, place, result)
        result = self.answerer.map_form(location, place, result)
        return result
