from textblob import TextBlob
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os 

load_dotenv()

NEWS_API_KEY = st.secrets.get("NEWS_API_KEY") or os.getenv("NEWS_API_KEY")

def get_average_polarity(ticker):

    api = NewsApiClient(api_key = NEWS_API_KEY)

    response = api.get_everything(
        q = ticker,
        language = "en",
        page_size = 20,
        sort_by = "relevancy"
        )

    total_polarity = 0

    for article in response["articles"]:
        articles_retrieved = article["title"]
        check_sentiment = TextBlob(articles_retrieved)
        polarity = check_sentiment.sentiment.polarity
        total_polarity += polarity

    if len(response["articles"]) == 0:
        st.error("There are no articles explictly mentioning this stock ticker.")
    
    else:
        return total_polarity / len(response["articles"])