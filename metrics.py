import pandas as pd 
import yfinance as yf
import math
import streamlit as st

# get data from user

def get_stock_data():

    ticker = st.text_input("Enter stock ticker: ").upper()
    period = st.text_input("Enter time period: ").lower()

    if ticker == "":
        st.stop()

    stock = yf.Ticker(ticker)
    df = stock.history(period = period).reset_index()

    if df.empty:
        st.error("Invalid ticker or period.")
        st.stop()

    return df, ticker

def moving_averages(df):
    df["50MA"] = df["Close"].ewm(span = 50, adjust = False).mean()
    df["200MA"] = df["Close"].ewm(span = 200, adjust = False).mean()
    return df


def daily_returns(df):
    df["Daily Return"] = df["Close"].pct_change() * 100
    return df

def find_beta(df, ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    beta = info.get("beta", None)
    return beta

# relative strength index
def rsi(df, length=14):
    delta = df["Close"].diff()

    gain = delta.where(delta > 0, 0)
    loss = delta.where(delta < 0, 0)

# use wilder's smoothing instead of normal rolling mean - gives more weight to recent days and less weight to older days

    avg_gain = gain.ewm(com=length-1, min_periods=length).mean()
    avg_loss = loss.abs().ewm(com=length-1, min_periods=length).mean()

    rs = avg_gain / avg_loss

    df["RSI"] = 100 - (100 / (1 + rs))
    return df["RSI"].iloc[-1]

def current_price(df):
    current_price = df["Close"].iloc[-1]
    return current_price

def yearly_hl(df, ticker):
    # ensure that if the time period selected by the user is less than 252 days, to generate a new df that is a year and calculate the high and low from that
    if len(df) < 252: 
        stock = yf.Ticker(ticker)
        df = stock.history(period = '1y').reset_index()

    df = df.tail(252)

    yearly_high = df["Close"].max()
    yearly_low = df["Close"].min()

    return yearly_high, yearly_low
    
def distance_yearly_high(df, ticker):
    yearly_high, yearly_low = yearly_hl(df, ticker)
    distance_from_high = ((df["Close"].iloc[-1] - yearly_high) / yearly_high) * 100
    return distance_from_high

import yfinance as yf
import pandas as pd

def fundamentals_df(ticker):
    stock = yf.Ticker(ticker)

    # Get financials (quarterly or yearly; use yearly for now)
    financials = stock.financials  # yearly financial statements
    info = stock.info             # general info (marketCap, PE ratio)

    # EPS
    eps = financials.loc["Basic EPS"].transpose().reset_index()
    eps.columns = ["Year", "EPS"]

    # Revenue
    revenue = financials.loc["Total Revenue"].transpose().reset_index()
    revenue.columns = ["Year", "Revenue"]

    # Net Income
    net_income = financials.loc["Net Income"].transpose().reset_index()
    net_income.columns = ["Year", "NetIncome"]

    # Merge all fundamentals by Year
    df_fundamentals = eps.merge(revenue, on = "Year", how = "outer").merge(net_income, on = "Year", how = "outer")
    df_fundamentals = df_fundamentals.sort_values("Year", ascending = True)

    # Add Market Cap & PE
    marketCap = info.get("marketCap", None)
    pe_ratio = info.get("trailingPE", None)

    return df_fundamentals, pe_ratio, marketCap

def calculate_all(df, ticker):
    df = moving_averages(df)
    df = daily_returns(df)

    beta = find_beta(df, ticker)
    rsi_val = rsi(df)
    price = current_price(df)
    yearly_high, yearly_low = yearly_hl(df, ticker)
    distance_from_high = distance_yearly_high(df, ticker)
    fund_df, pe_ratio, marketCap = fundamentals_df(ticker)
    return df, beta, rsi_val, price, yearly_high, yearly_low, distance_from_high, fund_df, pe_ratio, marketCap