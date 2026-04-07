import streamlit as st
import plotly.graph_objects as go
from main import run

st.set_page_config(page_title="Stock Analyzer", layout="wide")

df, ticker, beta, rsi_val, price, yearly_high, yearly_low, distance_from_high, fund_df, pe_ratio, marketCap = run()

# --- Header ---
st.title(f"{ticker} Stock Dashboard")
st.divider()

# --- Key Metrics Row ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Current Price", f"${price:.2f}")
col2.metric("52W High", f"${yearly_high:.2f}")
col3.metric("52W Low", f"${yearly_low:.2f}")
col4.metric("Distance from High", f"{distance_from_high:.2f}%")

st.divider()

# --- Second Metrics Row ---
col6, col7, col8, col9 = st.columns(4)
col6.metric("RSI (14)", f"{rsi_val:.2f}")
col7.metric("Beta", f"{beta:.4f}")
col8.metric("PE Ratio", f"{pe_ratio:.2f}")
col9.metric("Market Cap", f"{marketCap}")

st.divider()

# --- Price Chart ---
st.subheader("Price vs. Moving Averages")
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["Date"], y=df["Close"],
    name="Close", line=dict(color="white", width=2)
))
fig.add_trace(go.Scatter(
    x=df["Date"], y=df["50MA"],
    name="50 Day MA", line=dict(color="orange", width=1.5)
))
fig.add_trace(go.Scatter(
    x=df["Date"], y=df["200MA"],
    name="200 Day MA", line=dict(color="blue", width=1.5)
))

fig.update_layout(
    template="plotly_dark",
    hovermode="x unified",
    height=500,
    margin=dict(l=0, r=0, t=0, b=0)
)
st.plotly_chart(fig, use_container_width=True)

st.divider()

# --- RSI Chart ---
st.subheader("RSI vs. Price")

fig_rsi = go.Figure()

fig_rsi.add_trace(go.Scatter(
    x = df["Date"], 
    y = df["RSI"],
    name = "RSI", 
    line = dict(color="purple", width=1),
    yaxis = "y",
))

fig_rsi.add_trace(go.Scatter(
    x = df["Date"], 
    y = df["Close"],
    name = "Close", 
    line=dict(color="white", width=1),
    yaxis = "y2",
 ))

# rsi levels
fig_rsi.add_hline(y=70, line_dash="dash", line_color="red", annotation_text="Overbought")
fig_rsi.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="Oversold")

fig_rsi.update_layout(
    template="plotly_dark",
    height=500,
    margin=dict(l=0, r=0, t=0, b=0),

    yaxis = dict(
        title = "RSI",
        range = [0,100],
        showgrid = False,
    ),

    yaxis2 = dict(
        title = "Price",
        overlaying = "y",
        side = "right",
        showgrid = True,
        autorange = True,
    )
)

st.plotly_chart(fig_rsi, width = "stretch")

st.divider()

# --- Fundamentals Table ---
st.subheader("Fundamentals")
st.dataframe(
        fund_df.style.format({
        "Revenue": lambda x: f"{x/1e9:.2f}B",
        "NetIncome": lambda x: f"{x/1e9:.2f}B",
        "EPS": "${:.2f}",
    })
)

# Earnings Chart YoY
st.divider()

fig_yoy = go.Figure()

# --- Earnings & Revenue YoY Chart ---
st.subheader("Earnings & Revenue YoY")

fig_yoy = go.Figure()

fig_yoy.add_trace(go.Bar(
    x = fund_df["Year"],
    y = fund_df["Revenue"],
    name = "Revenue",
    marker_color = "light blue",
))
fig_yoy.add_trace(go.Bar(
    x = fund_df["Year"],
    y = fund_df["NetIncome"],
    name = "Net Income",
    marker_color = "orange",
))

fig_yoy.update_layout(
    template="plotly_dark",
    barmode="group",
    height=400,
    margin=dict(l=0, r=0, t=0, b=0),
    yaxis=dict(title="YoY"),
)

st.plotly_chart(fig_yoy, use_container_width=True)