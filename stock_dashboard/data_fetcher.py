import yfinance as yf
import pandas as pd

def fetch_data(ticker, period='1y', interval='1d', start=None, end=None):
    """
    Fetches historical data for a given ticker.

    Args:
        ticker (str): The stock or crypto ticker symbol (e.g., 'AAPL', 'BTC-USD').
        period (str): The data period to download (e.g., '1mo', '1y', 'ytd', 'max').
                      Ignored if start and end are provided.
        interval (str): The data interval (e.g., '1d', '1wk', '1m').
        start (str or datetime): Start date string (YYYY-MM-DD) or datetime object.
        end (str or datetime): End date string (YYYY-MM-DD) or datetime object.

    Returns:
        pd.DataFrame: A DataFrame containing the historical data. Returns None if data is empty or fetch fails.
    """
    try:
        # If start and end are provided, yfinance prioritizes them over period
        if start and end:
            data = yf.download(ticker, start=start, end=end, interval=interval, progress=False)
        else:
            data = yf.download(ticker, period=period, interval=interval, progress=False)
            
        # Flatten MultiIndex columns if present (common in recent yfinance versions)
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
            
        if data.empty:
            return None
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
