import requests
import json


try:
    f = open('data-base/keys.json')
    data = json.load(f)
    API_KEY = data['api_key']
    SEARCH_ENGINE_ID = data['engine_id']  
except KeyError as error:
    print(error)


def search_item(query_item:str):
    query = query_item
    page = 1
    start = (page - 1) * 10 + 1

    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

    data = requests.get(url).json()
    search_items = data.get("items")

    # iterate over 10 results found
    for i, search_item in enumerate(search_items, start=1):
        separations = "=" * 10, f"Result#{i + start - 1}", "=" * 10
        titles = search_item.get("title")

        snippets = search_item.get("snippet")
        links = search_item.get("link")

        all = [separations, titles, '\n',snippets, '\n', links, '\n']

        with open('content/content.txt', 'a', encoding='utf-8') as f:
            for separation in all:
                print(separation)
                f.write(''.join(separation))
                f.write('\n')
