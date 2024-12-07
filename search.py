from abc import ABC, abstractmethod

class Search(ABC):
    @abstractmethod
    def search(self, query, start_page, pages, lang):
        pass

    @abstractmethod
    def get_query(self, query, start_page, pages, lang):
        pass

    @abstractmethod
    def custom_results(self, results):
        pass

