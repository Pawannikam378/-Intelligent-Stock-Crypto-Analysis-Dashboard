import pandas as pd
import numpy as np

def calculate_sma(data, window=20):
    """Calculates the Simple Moving Average (SMA)."""
    return data['Close'].rolling(window=window).mean()

def calculate_ema(data, window=20):
    """Calculates the Exponential Moving Average (EMA)."""
    return data['Close'].ewm(span=window, adjust=False).mean()

def calculate_rsi(data, window=14):
    """Calculates the Relative Strength Index (RSI)."""
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(data, slow=26, fast=12, signal=9):
    """Calculates the Moving Average Convergence Divergence (MACD)."""
    exp1 = data['Close'].ewm(span=fast, adjust=False).mean()
    exp2 = data['Close'].ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

def calculate_bollinger_bands(data, window=20, no_of_std=2):
    """Calculates Bollinger Bands."""
    sma = data['Close'].rolling(window=window).mean()
    std = data['Close'].rolling(window=window).std()
    upper_band = sma + (std * no_of_std)
    lower_band = sma - (std * no_of_std)
    return upper_band, lower_band
