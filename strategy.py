from indicators import calculate_bollinger_bands, calculate_z_score

def apply_strategy(data):
    data['SMA_20'] = calculate_sma(data['Close'], window=20)
    data['SMA_50'] = calculate_sma(data['Close'], window=50)
    data['Z_Score'] = calculate_z_score(data['Close'], window=20)
    data['BB_Upper'], data['BB_Lower'] = calculate_bollinger_bands(data['Close'], window=20, num_std_dev=2)
    return data
