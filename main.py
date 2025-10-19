from news_agent import NewsAgent
from sentiment_agent import SentimentAgent
from stock_agent import StockAgent
from nn_agent import TradingNN
import torch


if __name__ == "__main__":
    keyword = input("Bitte UN eingeben: ")
    news_agent = NewsAgent()
    articles = news_agent.get_news(keyword)

    agent = SentimentAgent()
    agent.perceive(articles)
    sentiment = float(agent.think())
    agent.act() #Aktion mit Sentiment printet hier



    stock_agent = StockAgent(keyword)
    data = stock_agent.getStockData()
    closeValues = [float(entry['close']) for entry in data]
    print(closeValues[0])


    model = TradingNN()
    valueChange = closeValues[1] - closeValues[0]
    x = torch.tensor([[sentiment,valueChange]], dtype=torch.float32)
    pred = model(x)
    action = ["BUY", "HOLD", "SELL"][torch.argmax(pred)]
    print(action)


