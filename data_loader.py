import yfinance as yf
import pandas as pd

def load_data(tickers, start_date="2020-01-01", end_date="2024-01-01"):
    data = {}
    for ticker in tickers:
        df = yf.download(ticker, start=start_date, end=end_date)
        data[ticker] = df
    return data
