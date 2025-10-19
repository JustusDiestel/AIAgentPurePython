from dotenv import load_dotenv
import os as os
import requests

''' Hier die DOCU der API: https://marketstack.com/documentation_v2 
    
    Eigentlich brauch ich hier noch eine API / AI-Agent der mir das keyword in den richtigen Börsenkürtzel umwandel! oder eine Map mit den S&P500
'''


class StockAgent():
    def __init__(self, keyword):
        load_dotenv()
        self.keyword = keyword
        self.api_key = os.getenv("MARKETSTACK_API_KEY")
        self.url = "https://api.marketstack.com/v2/eod"


    def getStockData(self):
        params = {
            "access_key": self.api_key,
            "symbols": self.keyword,
            "limit": 5,
            "sort": "DESC",
        }
        response = requests.get(self.url, params=params )
        if response.status_code != 200:
            print("Fehler beim Laden der News:", response.text)
            return []
        else:
            data = response.json()
            if "data" in data:
                return data["data"]
            else:
                print("Fehlerhafte Antwort:", data)
                return []

    #def getMarktSegmentData(self):
