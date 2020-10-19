from tqdm import tqdm

from kocrawl.searcher.base_searcher import BaseSearcher


class DaumNewsSearcher(BaseSearcher):
    def __init__(self):
        self.replace = ["1)", "2)", "3)", "4)", "5)", "6)", "7)", "8)", "9)", "@"]
        self.selectors = [[".list_news2 > li > .cont_thumb > .tit_thumb > .link_txt"], ["section > p"]]

    def _make_query(self):
        return None

    def search_daum_news(self, top_n: int) -> tuple:
        result = self._bs4_documents(
            url=self.url["daum_news"], selectors=self.selectors[0]
        )

        articles = []
        urls = [res.get("href") for res in result]
        urls_output = []
        for url in tqdm(urls):
            if len(articles) >= top_n:
                break

            search = self._bs4_contents(url, selectors=self.selectors[1])

            sentences = ""
            for s in search:
                sentences += self._untag(str(s[0]))

            if len(sentences) > 300:
                articles.append(sentences)
                urls_output.append(url)

        return articles, urls_output
