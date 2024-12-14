import requests
from strategys.search import Search

class GoogleSearch(Search):
    def __init__(self, api_key, search_engine):
        super().__init__()
        self.api_key = api_key
        self.search_engine = search_engine

    
    def search(self, query, start_page=1, pages=1, lang="lang_es"):
        final_result = []
        url = self.get_query(query, start_page, pages, lang)
        results_per_page = 10
        for page in range(pages):
            start_index = (start_page - 1) * results_per_page + 1 + (page * results_per_page)
            url = self.get_query(query, start_index, pages, lang)
            response = requests.get(url)
            if response.status_code == 200 :
                data = response.json()
                results = data.get('items')
                cresults = self.custom_results(results)
                final_result.extend(cresults)
            else :
                print(f"Error al obtener la data, status: {response.status_code}")
                break
        return final_result
    

    def get_query(self, query, start_page, pages, lang):
        return f"https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.search_engine}&q={query}&start={start_page}&lr={lang}"
    
    def custom_results(self, results):
        custom_results = []
        for r in results :
            cresult = {}
            cresult["title"] = r.get('title')
            cresult["link"] = r.get('link')
            cresult["description"] = r.get('snippet')
            # print(r.get('title'), r.get('link'), sep=" - ")
            # print("\n")
            custom_results.append(cresult)
        return custom_results