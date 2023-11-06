# Filename: main.py

from get_arxiv import get_arxiv
from format_paper import format_paper
import json

with open('config.json') as f:
    config = json.load(f)

def main():
    title, abstract = get_arxiv("machine learning")
    api_key = config['openai_api_key']
    summary = format_paper(title, abstract, api_key)
    print(summary)


if __name__ == "__main__":
    main()
