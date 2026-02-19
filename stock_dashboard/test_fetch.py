from data_fetcher import fetch_data
import pandas as pd

try:
    data = fetch_data('AAPL', period='1mo')
    if data is None:
        print("Data fetch failed")
        exit(1)
        
    print("Columns:", data.columns)
    print("Shape:", data.shape)
    
    # Check if 'Close' is in columns
    if 'Close' not in data.columns:
        print("Error: 'Close' column missing. Columns are:", data.columns)
        exit(1)
        
    # Check for MultiIndex
    if isinstance(data.columns, pd.MultiIndex):
        print("Error: Columns are MultiIndex")
        exit(1)
        
    print("Test Passed: Columns are flat and contain 'Close'.")
except Exception as e:
    print(f"Test Failed with error: {e}")
    exit(1)
