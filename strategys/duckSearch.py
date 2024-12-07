import requests
from search import Search

class DuckSearch(Search):
    def __init__(self, api_key):
        super().__init__()
        self.api_key = api_key

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
                if data.get('error') :
                    print(data.get('error'))
                    return
                results = data.get('organic_results')
                cresults = self.custom_results(results)
                final_result.extend(cresults)
            else :
                print(f"Error al obtener la data, status: {response.status_code}")
                break
        return final_result

    def get_query(self, query, start_page, pages, lang):
        return f"https://serpapi.com/search?engine=duckduckgo&q={query}&api_key={self.api_key}"

    def custom_results(self, results):
        custom_results = []
        for r in results :
            cresult = {}
            cresult["title"] = r.get('title')
            cresult["link"] = r.get('link')
            cresult["description"] = r.get('snippet')
            print(r.get('title'), r.get('link'), sep=" - ")
            print("\n")
            custom_results.append(cresult)
        return custom_results