from dotenv import load_dotenv, set_key
import os
from strategys.googleSearch import GoogleSearch 
from strategys.duckSearch import DuckSearch
from strategys.strategy import StrategySearch
from utils.results_parser import ResultsParser


load_dotenv()

apiKey_google_search = os.getenv("APIKEY_GOOGLE")

apikey_duckgo = os.getenv("APIKEY_DUCKGO")

search_engine_id = os.getenv("SEARCH_ENGINE")

query = 'filetype:sql "Mysql dump" (pass|password|passwd|pwd) '

page=1

pages=2

lang = "lang_es"

def main(query, start_page, pages, lang):

    if not apiKey_google_search or not search_engine_id or not apikey_duckgo :
        print('no hay api keys de env')
        add_envs()

    strategyGoogle = StrategySearch(GoogleSearch(apiKey_google_search, search_engine_id))

    resultGoogle = strategyGoogle.executeSearch(query, start_page, pages)

    data = ResultsParser(resultGoogle)

    data.export_html('google.html')

    #print('google result', resultGoogle)

    #strategyGoogle = StrategySearch(DuckSearch(apikey_duckgo))

    #resultDuck = strategyGoogle.executeSearch(query, start_page, pages)

    #print('duck result', resultDuck)


def add_envs():
    api_key_google = input('Indica tu api key de google: ')
    set_key('.env', 'APIKEY_GOOGLE', api_key_google)

    search_engine_id = input('Indica tu search engine id de google: ')
    set_key('.env', 'SEARCH_ENGINE', search_engine_id)

    api_key_duck = input('Indica tu api key de duck duck: ')
    set_key('.env', 'APIKEY_DUCKGO', api_key_duck)
