from search import Search

class StrategySearch:
    def __init__(self, strategy: Search):
        self.strategy = strategy

    def executeSearch(self, query, start_page=1, pages=1, lang="lang_es"):
        return self.strategy.search(query, start_page, pages, lang)
