# import yfinance as yf

# stock = yf.Ticker("MSFT")

# financials = stock.financials

# print(financials)

from textblob import TextBlob
wiki = TextBlob("I hate coding.")

print(wiki.sentiment)
