from dotenv import load_dotenv
import os
from strategys.googleSearch import GoogleSearch 
from strategys.duckSearch import DuckSearch
from strategy import StrategySearch

load_dotenv()

apiKey_google_search = os.getenv("APIKEY_GOOGLE")

apikey_duckgo = os.getenv("APIKEY_DUCKGO")

search_engine_id = os.getenv("SEARCH_ENGINE")

query = "filetype:sql 'Mysql dump' (pass|password|passwd|pwd) "

page=1

pages=2

lang = "lang_es"

def main():
    strategyGoogle = StrategySearch(GoogleSearch(apiKey_google_search, search_engine_id))

    resultGoogle = strategyGoogle.executeSearch(query, page, pages)

    print('google result', resultGoogle)

    strategyGoogle = StrategySearch(DuckSearch(apikey_duckgo))

    resultDuck = strategyGoogle.executeSearch(query, page, pages)

    print('duck result', resultDuck)

main()



