import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of the selected company!
""")

# Input for the ticker symbol
tickerSymbol = st.text_input(
    "Enter a ticker symbol (e.g., AAPL, GOOG, MSFT):", "PLUG")

# Ensure a ticker symbol is entered
if tickerSymbol:
    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    # Get the company's full name
    companyName = tickerData.info['longName']
    # Get the historical prices for this ticker
    tickerDf = tickerData.history(
        period='1d', start='2010-5-31', end='2024-5-31')

    if not tickerDf.empty:
        st.write(f"Showing data for {companyName} ({tickerSymbol})")
        st.line_chart(tickerDf.Close)
        st.line_chart(tickerDf.Volume)
    else:
        st.write(
            "No data found for the entered ticker symbol. Please try another symbol.")
