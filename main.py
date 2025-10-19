from news_agent import NewsAgent
from sentiment_agent import SentimentAgent
from stock_agent import StockAgent


if __name__ == "__main__":
    keyword = input("Bitte UN eingeben: ")
    news_agent = NewsAgent()
    articles = news_agent.get_news(keyword)

    agent = SentimentAgent()
    sentiment = agent.perceive(articles)
    agent.act() #Aktion mit Sentiment printet hier



    stock_agent = StockAgent(keyword)
    print(stock_agent.getStockData()[0]['close'])


