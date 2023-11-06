import requests

def get_arxiv(keywords):
    url = 'http://export.arxiv.org/api/query'
    params = {
        'search_query': f'all:{keywords}',
        'start': 0,
        'max_results': 1
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    feed = response.text
    entry = feed.split('<entry>')[1]
    title = entry.split('<title>')[1].split('</title>')[0]
    abstract = entry.split('<summary>')[1].split('</summary>')[0]
    return title, abstract

