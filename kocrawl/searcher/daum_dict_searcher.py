from tqdm import tqdm

from kocrawl.searcher.base_searcher import BaseSearcher


class DaumDictSearcher(BaseSearcher):
    def __init__(self):
        self.replace = ["1)", "2)", "3)", "4)", "5)", "6)", "7)", "8)", "9)"]
        self.selectors = [[".tit_hotissues"], [".desc_section"]]

    def _make_query(self):
        return None

    def search_daum_dict(self, top_n: int) -> tuple:
        result = self._bs4_contents(
            url=self.url["daum_dict"], selectors=self.selectors[0]
        )
        result = (
            (self.url["daum_dict"] + i[1].get("href"), i[1].string) for i in result
        )

        cache_dict = {}
        keywords = set()
        urls = {}
        for url, keyword in tqdm(result):
            keywords.add(keyword)
            if len(keywords) > top_n:
                break

            urls[keyword] = url
            document = self._bs4_contents(url=url, selectors=self.selectors[1])
            for paragraph in document:
                for sentence in paragraph:
                    sentence = self._untag(sentence)

                    if keyword not in cache_dict:
                        cache_dict[keyword] = sentence
                    else:
                        cache_dict[keyword] += sentence

        output_list, url_list = [], []
        for o in cache_dict.items():
            keyword = o[0]
            context = o[1].split("\r")[0]
            for rep in self.replace:
                context = context.replace(rep, "")
            context = context.replace("  ", " ")

            if keyword in context:
                output_list.append((keyword, context))
                url_list.append(urls[keyword])

        return output_list, url_list
