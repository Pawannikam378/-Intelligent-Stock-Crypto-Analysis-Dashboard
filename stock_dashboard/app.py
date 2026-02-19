import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_fetcher import fetch_data
from indicators import calculate_sma, calculate_ema, calculate_rsi, calculate_macd, calculate_bollinger_bands
from strategy import generate_signals, backtest
from risk import calculate_volatility, calculate_max_drawdown, calculate_sharpe_ratio

# Page Configuration
st.set_page_config(page_title="Intelligent Stock & Crypto Dashboard", layout="wide")

st.title("Intelligent Stock & Crypto Analysis Dashboard")

# Sidebar for User Inputs
st.sidebar.header("User Input Parameters")
ticker = st.sidebar.text_input("Ticker Symbol", value="AAPL")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("today"))
interval = st.sidebar.selectbox("Interval", options=["1d", "1wk"], index=0)

initial_investment = st.sidebar.number_input("Initial Investment in (INR)", value=10000.0)

# Fetch Data
if st.sidebar.button("Analyze"):
    st.write(f"Fetching data for {ticker} from {start_date} to {end_date}...")
    
    data = fetch_data(ticker, start=start_date, end=end_date, interval=interval)
    
    if data is None or data.empty:
        st.error(f"No data found for {ticker}. Please check the symbol and date range.")
    else:
        st.success(f"Data loaded successfully! {len(data)} rows.")
        
        # Calculate Indicators
        data['SMA'] = calculate_sma(data)
        data['EMA'] = calculate_ema(data)
        data['RSI'] = calculate_rsi(data)
        macd, signal_line = calculate_macd(data)
        data['MACD'] = macd
        data['Signal_Line'] = signal_line
        upper, lower = calculate_bollinger_bands(data)
        data['Upper_Band'] = upper
        data['Lower_Band'] = lower
        
        # Generate Signals
        # Ensure sufficient data for indicators
        data = data.dropna()
        signals = generate_signals(data)
        
        # Backtest
        backtest_result, strategy_final_val, buy_hold_final_val = backtest(data, signals, initial_investment)
        
        # Risk Metrics
        volatility = calculate_volatility(data)
        max_dd = calculate_max_drawdown(data)
        sharpe = calculate_sharpe_ratio(data)
        
        # --- Visualization ---
        
        # 1. Price Chart with Indicators & Buy/Sell Markers
        st.subheader("Price Chart & Technical Indicators")
        fig1, ax1 = plt.subplots(figsize=(14, 7))
        ax1.plot(data.index, data['Close'], label='Close Price', alpha=0.5)
        ax1.plot(data.index, data['SMA'], label='SMA (20)', color='orange', linestyle='--')
        ax1.plot(data.index, data['Upper_Band'], label='Upper BB', color='green', linestyle=':', alpha=0.3)
        ax1.plot(data.index, data['Lower_Band'], label='Lower BB', color='red', linestyle=':', alpha=0.3)
        ax1.fill_between(data.index, data['Upper_Band'], data['Lower_Band'], color='gray', alpha=0.1)
        
        # Buy/Sell Markers
        buy_signals = signals[signals['signal'] == 1.0]
        sell_signals = signals[signals['signal'] == -1.0]
        
        ax1.scatter(buy_signals.index, buy_signals['price'], marker='^', color='green', label='Buy Signal', s=100, zorder=5)
        ax1.scatter(sell_signals.index, sell_signals['price'], marker='v', color='red', label='Sell Signal', s=100, zorder=5)
        
        ax1.set_title(f"{ticker} Price Analysis")
        ax1.set_xlabel("Date")
        ax1.set_ylabel("Price")
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        st.pyplot(fig1)
        
        # 2. RSI Chart
        st.subheader("Relative Strength Index (RSI)")
        fig2, ax2 = plt.subplots(figsize=(14, 4))
        ax2.plot(data.index, data['RSI'], label='RSI', color='purple')
        ax2.axhline(70, linestyle='--', color='red', alpha=0.5)
        ax2.axhline(30, linestyle='--', color='green', alpha=0.5)
        ax2.set_title("RSI Indicator")
        ax2.set_ylim(0, 100)
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        st.pyplot(fig2)

        # 3. MACD Chart
        st.subheader("MACD")
        fig3, ax3 = plt.subplots(figsize=(14, 4))
        ax3.plot(data.index, data['MACD'], label='MACD', color='blue')
        ax3.plot(data.index, data['Signal_Line'], label='Signal Line', color='orange')
        ax3.bar(data.index, data['MACD'] - data['Signal_Line'], label='Histogram', color='gray', alpha=0.3)
        ax3.set_title("MACD Indicator")
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        st.pyplot(fig3)
        
        # 4. Portfolio Performance
        st.subheader("Portfolio Performance")
        col1, col2 = st.columns(2)
        col1.metric("Strategy Final Value", f"₹{strategy_final_val:,.2f}")
        col2.metric("Buy & Hold Final Value", f"₹{buy_hold_final_val:,.2f}")
        
        fig4, ax4 = plt.subplots(figsize=(14, 5))
        ax4.plot(backtest_result.index, backtest_result['Portfolio Value'], label='Strategy Portfolio', color='blue')
        
        # Create a Buy & Hold equity curve for comparison visualization
        initial_price = backtest_result['Close'].iloc[0]
        buy_hold_equity = (backtest_result['Close'] / initial_price) * initial_investment
        ax4.plot(backtest_result.index, buy_hold_equity, label='Buy & Hold', color='gray', linestyle='--')
        
        ax4.set_title("Portfolio Growth Over Time")
        ax4.set_xlabel("Date")
        ax4.set_ylabel("Value (INR)")
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        st.pyplot(fig4)
        
        # 5. Risk Metrics
        st.subheader("Risk Metrics")
        m1, m2, m3 = st.columns(3)
        m1.metric("Annualized Volatility", f"{volatility:.2%}")
        m2.metric("Max Drawdown", f"{max_dd:.2%}")
        m3.metric("Sharpe Ratio", f"{sharpe:.2f}")

        # Raw Data Expander
        with st.expander("View Raw Data"):
            st.dataframe(data.tail(10))

else:
    st.info("Select parameters and click 'Analyze' to start.")
