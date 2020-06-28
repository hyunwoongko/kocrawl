from kocrawl.answerer.dust_answerer import DustAnswerer
from kocrawl.base import BaseCrawler
from kocrawl.editor.dust_editor import DustEditor
from kocrawl.searcher.dust_searcher import DustSearcher


class DustCrawler(BaseCrawler):

    def __init__(self):
        super().__init__()
        self.date_coverage = self.date['today'] + \
                             self.date['tomorrow'] + \
                             self.date['after']

    def request(self, location: str, date: str):
        """
        미세먼지를 크롤링합니다.
        (try-catch로 에러가 나지 않는 함수)

        :param location: 지역
        :param date: 날짜
        :return: 해당지역 날짜 미세먼지
        """

        try:
            return self.request_debug(location, date)[0]
        except Exception:
            return DustAnswerer().sorry(
                "해당 대기 오염정보는 알 수 없습니다."
            )

    def request_dict(self, location: str, date: str):
        """
        미세먼지를 크롤링합니다.
        (try-catch로 에러가 나지 않는 함수)

        :param location: 지역
        :param date: 날짜
        :return: 해당지역 날짜 미세먼지
        """

        try:
            return self.request_debug(location, date)[1]
        except Exception:
            return DustAnswerer().sorry(
                "해당 대기 오염정보는 알 수 없습니다."
            )

    def request_debug(self, location: str, date: str):
        """
        미세먼지를 크롤링합니다.
        (에러가 나는 디버깅용 함수)

        :param location: 지역
        :param date: 날짜
        :return: 해당지역 날짜 미세먼지
        """

        return self.__new_everyday(location, date)

    def __new_everyday(self, location: str, date: str) -> tuple:
        """
        네이버 미세먼지는 신/구버전이 있는데,
        주요 도시는 신버전으로, 군/구/읍/면/동 등 시 이하의 행정구역은 구버전으로 구현되어있음.
        우선 신버전(오늘,내일,모레)으로 검색한 뒤  실패시 구버전 검색 시도

        :param location: 지역
        :param date: 날짜
        :return: 해당지역 날짜 미세먼지
        """

        try:
            result_dict = DustSearcher().new_everyday(location, date)
            result, josa = DustEditor().edit_morning_afternoon(location, date, result_dict)
            return DustAnswerer().morning_afternoon_form(location, date, result, josa), result_dict
        except Exception:
            return self.__old_version(location, date)

    def __old_version(self, location: str, date: str) -> tuple:
        """
        네이버 미세먼지는 신/구버전이 있는데,
        주요 도시는 신버전으로, 군/구/읍/면/동 등 시 이하의 행정구역은 구버전으로 구현되어있음.
        신버전에서 실패할시 구버전으로 검색을 시도함 (날짜에 따라 오늘, 내일/모레 뷰가 다름)

        :param location: 지역
        :param date: 날짜
        :return: 해당지역 날짜 미세먼지
        """

        if date in self.date['today']:
            return self.__old_today(location, date)
        else:
            return self.__old_tomorrow(location, date)

    def __old_today(self, location: str, date: str) -> tuple:
        """
        네이버 미세먼지는 신/구버전이 있는데,
        주요 도시는 신버전으로, 군/구/읍/면/동 등 시 이하의 행정구역은 구버전으로 구현되어있음.
        신버전에서 실패할시 구버전(오늘) 검색을 시도함.

        :param location: 지역
        :param date: 날짜
        :return: 해당지역 날짜 미세먼지
        """

        result_dict = DustSearcher().old_today(location, date)
        result, josa = DustEditor().edit_single(location, date, result_dict)
        return DustAnswerer().single_form(location, date, result, josa), result_dict

    def __old_tomorrow(self, location: str, date: str) -> tuple:
        """
        네이버 미세먼지는 신/구버전이 있는데,
        주요 도시는 신버전으로, 군/구/읍/면/동 등 시 이하의 행정구역은 구버전으로 구현되어있음.
        신버전에서 실패할시 구버전(내일/모레) 검색을 시도함.

        :param location: 지역
        :param date: 날짜
        :return: 해당지역 날짜 미세먼지
        """

        result_dict = DustSearcher().old_tomorrow(location, date)
        result, josa = DustEditor().edit_morning_afternoon(location, date, result_dict)
        return DustAnswerer().morning_afternoon_form(location, date, result, josa), result_dict
