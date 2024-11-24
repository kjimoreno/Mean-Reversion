import pandas as pd
import numpy as np

def backtest_strategy(data, initial_cash=10000):
    cash = initial_cash
    position = 0
    portfolio_value = []

    for i in range(1, len(data)):
        if data['Close'].iloc[i] < data['BB_Lower'].iloc[i] and position == 0:
            position = cash // data['Close'].iloc[i]  
            cash -= position * data['Close'].iloc[i]  
        
        elif data['Close'].iloc[i] > data['BB_Upper'].iloc[i] and position > 0:
            cash += position * data['Close'].iloc[i]  
            position = 0  

        portfolio_value.append(cash + position * data['Close'].iloc[i])

    return portfolio_value
