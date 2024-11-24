import pandas as pd
import numpy as np

def calculate_sma(series, window):
    return series.rolling(window=window).mean()

def calculate_bollinger_bands(series, window=20, num_std_dev=2):
    rolling_mean = series.rolling(window=window).mean()
    rolling_std = series.rolling(window=window).std()
    upper_band = rolling_mean + (rolling_std * num_std_dev)
    lower_band = rolling_mean - (rolling_std * num_std_dev)
    return upper_band, lower_band

def calculate_z_score(series, window=20):
    mean = series.rolling(window).mean()
    std = series.rolling(window).std()
    z_score = (series - mean) / std
    return z_score
