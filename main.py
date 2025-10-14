from news_agent import NewsAgent
from sentiment_agent import SentimentAgent

if __name__ == "__main__":
    keyword = input("Bitte UN eingeben: ")
    news_agent = NewsAgent()
    articles = news_agent.get_news(keyword)

    agent = SentimentAgent()
    agent.perceive(articles)
    agent.act()