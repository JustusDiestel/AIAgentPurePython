from transformers import pipeline
import datetime
'''
# Das hier ist nur code - kein AI Agent
class SentimentAgent:
    def __init__(self):
        self.analyzer = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def analyze_articles(self, articles):
        results = []
        for a in articles:
            sentiment = self.analyzer(a["title"])[0]
            a["sentiment"] = sentiment["label"]
            a["score"] = sentiment["score"] #der score ist btw eine Warhscheinlichkeit
            results.append(a)
        return results
'''

class SentimentAgent:
    def __init__(self, model="distilbert-base-uncased-finetuned-sst-2-english"):
        self.analyzer = pipeline("sentiment-analysis", model=model)
        self.memory = []
        self.decay_rate = 0.9

    def perceive(self, articles):
        """nimmt neue Artikel wahr und analysiert sie"""
        for a in articles:
            sentiment = self.analyzer(a["title"])[0]
            entry = {
                "title": a["title"],
                "sentiment": 1 if sentiment["label"] == "POSITIVE" else -1,
                "score": sentiment["score"],
                "published": a["published"],
                "timestamp": datetime.datetime.now()
            }
            self.memory.append(entry)

    def think(self):
        now = datetime.datetime.now()
        weighted_sum, total_weight = 0, 0

        for entry in self.memory:
            age_days = (now - entry["timestamp"]).days
            weight = self.decay_rate ** age_days
            weighted_sum += entry["sentiment"] * entry["score"] * weight
            total_weight += weight

        avg_sentiment = weighted_sum/ total_weight if total_weight else 0
        return avg_sentiment

    def act(self):
        trend = self.think()
        if trend > 0.2:
            print(f" Marktstimmung POSITIV ({trend:.2f})")
        elif trend < -0.2:
            print(f" Marktstimmung NEGATIV ({trend:.2f})")
        else:
            print(f" Marktstimmung NEUTRAL ({trend:.2f})")
