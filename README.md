# 📈 Stock Analyzer Dashboard

A Python-based stock analysis dashboard built with Streamlit that pulls real market data and provides technical indicators, risk metrics, and news sentiment analysis for any publicly traded stock.

---

## 🔗 Live Demo

[Click here to open the app](your-streamlit-url-here)

---

## 📊 Features

- Interactive price chart with 50-day and 200-day moving averages
- RSI momentum indicator with overbought/oversold signals
- Annualized volatility and Sharpe ratio
- Daily returns distribution
- Real-time news sentiment analysis using NLP

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| pandas | Data manipulation |
| yfinance | Market data fetching |
| Plotly | Interactive charts |
| Streamlit | Dashboard UI |
| NewsAPI | Financial headlines |
| TextBlob | Sentiment analysis |

---

## 🚀 How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/eesh4n/stock-analyzer.git
cd stock-analyzer
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your API key**

Create a `.env` file in the root directory:
```
NEWS_API_KEY=your_key_here
```

**4. Run the app**
```bash
streamlit run charts.py
```

---

## 📁 Project Structure

```
stock_analyzer/
├── charts.py       # Streamlit dashboard UI
├── main.py         # Entry point, wires everything together
├── metrics.py      # Technical indicators (RSI, MA, beta, fundamentals)
├── sentiment.py    # News fetching and sentiment scoring
├── .env            # API keys (not tracked by git)
├── .gitignore
└── requirements.txt
```

---

## 📸 Screenshots

*Add screenshots of your dashboard here*

---

## ⚠️ Limitations

- Sentiment is scored on headlines only using TextBlob, which may not fully capture financial context
- Free NewsAPI tier limits to 100 requests/day
- Fundamental data availability depends on yfinance coverage for the given ticker
