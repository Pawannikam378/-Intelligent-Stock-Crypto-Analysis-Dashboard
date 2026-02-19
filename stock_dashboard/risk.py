import numpy as np
import pandas as pd

def calculate_volatility(data):
    """Calculates annualized volatility."""
    # Annualized volatility = Standard Deviation of daily returns * sqrt(252)
    daily_returns = data['Close'].pct_change()
    volatility = daily_returns.std() * np.sqrt(252)
    return volatility

def calculate_max_drawdown(data):
    """Calculates Maximum Drawdown."""
    # Roll max
    # We use 'Close' price for this calculation
    roll_max = data['Close'].cummax()
    daily_drawdown = data['Close'] / roll_max - 1.0
    max_drawdown = daily_drawdown.min()
    return max_drawdown

def calculate_sharpe_ratio(data, risk_free_rate=0.05):
    """Calculates Sharpe Ratio."""
    # Sharpe Ratio = (Mean Daily Return - Risk Free Rate) / Std Dev of Daily Returns
    # Note: risk_free_rate is usually annual. We verify if we need to adjust it to daily.
    # Daily RF = (1 + Annual RF)^(1/252) - 1 approx Annual RF / 252
    
    daily_rf = risk_free_rate / 252
    daily_returns = data['Close'].pct_change()
    
    mean_daily_return = daily_returns.mean()
    std_daily_return = daily_returns.std()
    
    if std_daily_return == 0:
        return 0
    
    sharpe_ratio = (mean_daily_return - daily_rf) / std_daily_return
    # Annualize it
    sharpe_ratio_annualized = sharpe_ratio * np.sqrt(252)
    
    return sharpe_ratio_annualized
