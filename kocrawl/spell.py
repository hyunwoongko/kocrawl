"""
@auther Hyunwoong
@since 6/29/2020
@see https://github.com/gusdnd852
"""
import json
import re

from requests import Session


class SpellCrawler:

    def request(self, text: str) -> str:
        """
        맞춤법을 교정합니다.
        (try-catch로 에러가 나지 않는 함수)

        :param text: 교정할 문자열
        :return: 교정된 문자열
        """

        try:
            return self.request_debug(text)[0]
        except Exception:
            return "해당 문자열은 교정할 수 없습니다."

    def request_dict(self, text: str) -> str:
        """
        맞춤법을 교정합니다.
        (try-catch로 에러가 나지 않는 함수)

        :param text: 교정할 문자열
        :return: 교정된 문자열
        """

        try:
            return self.request_debug(text)[1]
        except Exception:
            return "해당 문자열은 교정할 수 없습니다."

    def request_debug(self, text: str) -> tuple:
        """
        ajax 크롤링을 이용하여 네이버 맞춤법 검사기 API를 사용합니다.

        :param text: 교정할 문자열
        :return: 교정된 문자열
        """

        if len(text) > 500:
            raise Exception('500글자 이상 넘을 수 없음!')

        sess = Session()
        data = sess.get(
            url='https://m.search.naver.com/p/csearch/ocontent/spellchecker.nhn',
            params={
                '_callback':
                    'window.__jindo2_callback._spellingCheck_0',
                'q': text},
            headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'referer': 'https://search.naver.com/'
            }
        )

        data = json.loads(data.text[42:-2])  # json 파싱
        html = data['message']['result']['html']  # 원하는부분 가져오기
        html = re.sub(re.compile('<.*?>'), '', html)
        errors = data['message']['result']['errata_count']

        result_dict = {
            'original': text,
            'checked': html,
            'errors': errors,
        }

        return html, result_dict
