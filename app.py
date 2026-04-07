import streamlit as st
import pandas as pd
from data import fetch_stock_data
from metrics import calculate_all
from charts import build_all_charts

st.set_page_config(
    page_title = "Stock Analyzer",
    page_icon = '📈',
    layout = "wide",
)

st.title("📈 Stock Analyzer Dashboard")
st.markdown("Analyze any stock's performance, risk, and momentum in real time.")


