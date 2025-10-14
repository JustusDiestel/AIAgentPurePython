import os

import requests
from newsapi import NewsApiClient
from dotenv import load_dotenv

class NewsAgent:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("NEWS_API_KEY")
        self.url = "https://newsapi.org/v2/everything"

    # so sieht das dann aus: https://newsapi.org/v2/everything?q=Tesla&language=en&apiKey=DEIN_KEY
    def get_news(self, company: str, limit: int = 5):
        params = {
            "q": company,
            "language": "en",
            "sortBy": "relevancy",
            "pageSize": limit,
            "apiKey": self.api_key,
        }
        response = requests.get(self.url, params=params)
        if response.status_code != 200:
            print("Fehler beim Laden der News:", response.text)
            return []

        articles = response.json().get("articles", [])
        results = []
        for a in articles:
            results.append(
                {
                    "title": a["title"],
                    "source": a["source"]["name"],
                    "published": a["publishedAt"],
                    "url": a["url"],
                }
            )
        return results


