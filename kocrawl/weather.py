from kocrawl.answerer.weather_answerer import WeatherAnswerer
from kocrawl.base import BaseCrawler
from kocrawl.editor.weather_editor import WeatherEditor
from kocrawl.searcher.weather_searcher import WeatherSearcher


class WeatherCrawler(BaseCrawler):

    def request(self, location: str, date: str):
        """
        날씨를 크롤링합니다.
        (try-catch로 에러가 나지 않는 함수)

        :param location: 지역
        :param date: 날짜
        :return: 만들어진진 문장
       """

        try:
            return self.request_debug(location, date)[0]
        except Exception:
            return WeatherAnswerer().sorry(
                '그 날씨는 알 수가 없어요.'
            )

    def request_dict(self, location: str, date: str):
        """
        날씨를 크롤링합니다.
        (try-catch로 에러가 나지 않는 함수)

        :param location: 지역
        :param date: 날짜
        :return: 만들어진진 문장
       """

        try:
            return self.request_debug(location, date)[1]
        except Exception:
            return WeatherAnswerer().sorry(
                '그 날씨는 알 수가 없어요.'
            )

    def request_debug(self, location: str, date: str):
        """
        날씨를 크롤링합니다.
        (에러가 나는 디버깅용 함수)

        :param location: 지역
        :param date: 날짜
        :return: 만들어진진 문장
        """

        if date in self.date['today']:
            return self.__today(location)
        elif date in self.date['tomorrow']:
            return self.__tomorrow(location)
        elif date in self.date['after']:
            return self.__after(location)
        elif date in self.date['specific']:
            return self.__specific(location, date)
        else:
            return self.__specific(location, date)

    def __today(self, location: str) -> tuple:
        """
        오늘 날씨를 검색하고 조합합니다.

        :param location: 지역
        :return: 오늘 날씨
        """

        result_dict = WeatherSearcher().naver_search(location)
        result = WeatherEditor().edit_today(result_dict)
        return WeatherAnswerer().comparison_with_yesterday_form(location, "오늘", result), result_dict

    def __tomorrow(self, location: str) -> tuple:
        """
        내일 날씨를 검색하고 조합합니다.

        :param location: 지역
        :return: 내일 날씨
        """

        result_dict = WeatherSearcher().naver_search(location)
        result, josa = WeatherEditor().edit_tomorrow(result_dict)
        return WeatherAnswerer().morning_afternoon_form(location, "내일", result, josa), result_dict

    def __after(self, location: str) -> tuple:
        """
        모네 날씨를 검색하고 조합합니다.

        :param location: 지역
        :return: 모레 날씨
        """

        result_dict = WeatherSearcher().naver_search(location)
        result, josa = WeatherEditor().edit_after(result_dict)
        return WeatherAnswerer().morning_afternoon_form(location, "모레", result, josa), result_dict

    def __specific(self, location: str, date: str) -> tuple:
        """
        특정 날짜 (e.g. 수요일, 6월 20일 등)의
        날씨를 검색하고 조합합니다.

        :param location: 지역
        :return: 오늘 날씨
        """

        result_dict = WeatherSearcher().google_search(location, date)
        result = WeatherEditor().edit_specific(result_dict)
        return WeatherAnswerer().specific_date_form(location, date, result), result_dict
