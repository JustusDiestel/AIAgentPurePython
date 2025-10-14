from news_agent import NewsAgent


if __name__ == "__main__":
    agent = NewsAgent()
    news = agent.get_news(input("Bitte UN eingeben: "))
    for n in news:
        print(f"{n['published']} \n {n['title']} \n ({n['source']})")