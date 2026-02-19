import pandas as pd
import numpy as np

def generate_signals(data, window=20):
    """
    Generates Buy/Sell signals based on the strategy:
    - Buy: RSI < 30 AND Price crosses above MA
    - Sell: RSI > 70 AND Price crosses below MA
    """
    if data is None or data.empty:
        return None
    
    # Ensure indicators are present. If not, calculate them for signal generation.
    # Note: Using Simple Moving Average (SMA) as 'MA' for this strategy.
    
    # We need to recalculate or ensure 'SMA' and 'RSI' columns exist in data
    # passed to this function. Ideally, data should already have these.
    # But to be safe and modular, let's assume data has 'Close' and we can 
    # access 'SMA' and 'RSI' if they exist, or user should ensure they are there.
    # Implementation decision: The app.py will calculate indicators and pass the dataframe here.
    # checking if columns exist
    if 'SMA' not in data.columns or 'RSI' not in data.columns:
         raise ValueError("Dataframe must contain 'SMA' and 'RSI' columns")

    signals = pd.DataFrame(index=data.index)
    signals['price'] = data['Close']
    signals['signal'] = 0.0 # 0: No Signal, 1: Buy, -1: Sell

    # Shift columns to check for crossovers
    # Previous Price
    prev_price = data['Close'].shift(1)
    # Previous MA
    prev_sma = data['SMA'].shift(1)
    
    # Conditions
    # Buy: RSI < 30 AND Price crosses above MA (Prev Price < Prev MA and Curr Price > Curr MA)
    # Note: The requirement says "Buy when RSI < 30 AND price crosses above MA".
    # Usually this means RSI is currently < 30, and the crossover happens.
    
    buy_condition = (
        (data['RSI'] < 30) & 
        (prev_price < prev_sma) & 
        (data['Close'] > data['SMA'])
    )
    
    # Sell: RSI > 70 AND Price crosses below MA (Prev Price > Prev MA and Curr Price < Curr MA)
    sell_condition = (
        (data['RSI'] > 70) & 
        (prev_price > prev_sma) & 
        (data['Close'] < data['SMA'])
    )
    
    signals.loc[buy_condition, 'signal'] = 1.0
    signals.loc[sell_condition, 'signal'] = -1.0
    
    return signals

def backtest(data, signals, initial_investment=10000.0):
    """
    Simulates investment based on signals.
    """
    if data is None or signals is None:
        return None

    # Reset index to make iteration easier if needed, but vectorization is better.
    # We will simulate a simple portfolio.
    
    cash = initial_investment
    holdings = 0.0
    portfolio_value = []
    
    # We need to iterate to handle the sequential nature of trading (can't sell what you don't have)
    # merging signals with data for easier iteration
    
    backtest_data = data.join(signals['signal'], rsuffix='_sig')
    
    for index, row in backtest_data.iterrows():
        price = row['Close']
        signal = row['signal']
        
        if signal == 1.0: # Buy
            if cash > 0:
                # Buy as much as possible
                holdings = cash / price
                cash = 0.0
        elif signal == -1.0: # Sell
            if holdings > 0:
                # Sell everything
                cash = holdings * price
                holdings = 0.0
        
        # Calculate current value
        current_value = cash + (holdings * price)
        portfolio_value.append(current_value)
        
    backtest_data['Portfolio Value'] = portfolio_value
    
    # Buy and Hold Strategy for comparison
    initial_price = backtest_data['Close'].iloc[0]
    final_price = backtest_data['Close'].iloc[-1]
    
    buy_hold_holdings = initial_investment / initial_price
    buy_hold_final_value = buy_hold_holdings * final_price
    
    strategy_final_value = portfolio_value[-1]
    
    return backtest_data, strategy_final_value, buy_hold_final_value
