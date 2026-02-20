# 📈 Intelligent Stock & Crypto Analysis Dashboard

A quantitative analysis dashboard built using **Python, Streamlit, and financial analytics techniques**.

This project fetches real-time market data, computes technical indicators manually, generates buy/sell signals, performs backtesting, and evaluates portfolio risk metrics.

Designed to demonstrate data engineering, financial mathematics, and algorithmic thinking.

---

## 🚀 Live Demo

🔗 Demo Link: _(Add after deployment)_  

Run locally:

```bash
streamlit run app.py
```

---

## 🎯 Project Objective

This application simulates a mini quantitative trading analysis platform.

It allows users to:
- Analyze stocks or crypto assets
- Apply technical indicators
- Generate rule-based trading signals
- Backtest strategies
- Evaluate risk-adjusted returns

---

## ✨ Features

### 📊 Market Data
- Fetch historical stock or crypto data using `yfinance`
- Custom date range
- Select time interval

### 📈 Technical Indicators (Manually Implemented)
- 20-Day Moving Average (MA)
- Exponential Moving Average (EMA)
- Relative Strength Index (RSI)
- MACD
- Bollinger Bands

All calculations are implemented using **Pandas & NumPy**, not third-party trading libraries.

---

### 🔔 Buy/Sell Signal Generator

Strategy Example:
- BUY → RSI < 30 AND price crosses above MA
- SELL → RSI > 70 AND price crosses below MA

Signals are displayed directly on the price chart.

---

### 🧪 Backtesting Engine

- Simulates ₹10,000 initial investment
- Executes trades based on signals
- Calculates:
  - Final portfolio value
  - Total return %
  - Comparison with Buy-and-Hold strategy

---

### 📉 Risk Analysis

- Volatility (Standard Deviation of Returns)
- Maximum Drawdown
- Sharpe Ratio

These metrics help evaluate risk-adjusted performance.

---

## 🧠 Indicator Mathematics

### Moving Average (MA)
```
MA = Rolling Mean of Closing Prices
```

### Exponential Moving Average (EMA)
```
EMA_t = (Price_t × α) + EMA_(t-1) × (1 - α)
```

### RSI
```
RSI = 100 - (100 / (1 + RS))
```
Where:
- RS = Average Gain / Average Loss

### Sharpe Ratio
```
Sharpe Ratio = (Mean Return - Risk Free Rate) / Std Dev of Returns
```

---

## 🏗 Project Structure

```
market_dashboard/
│── app.py
│── data_fetcher.py
│── indicators.py
│── strategy.py
│── risk.py
│── utils.py
│── requirements.txt
│── README.md
```

---

## 🛠 Tech Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Data Handling | Pandas |
| Numerical Computing | NumPy |
| Visualization | Matplotlib |
| Market Data | yfinance |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/market-dashboard.git
cd market-dashboard
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## 📊 Example Output

- Asset: AAPL
- Final Portfolio Value: ₹13,450
- Total Return: +34.5%
- Sharpe Ratio: 1.42
- Max Drawdown: -12%

---

## 📈 What This Project Demonstrates

- Financial Data Analysis
- Manual Indicator Implementation
- Algorithmic Strategy Design
- Backtesting Logic
- Risk Evaluation
- Data Visualization
- Modular Code Architecture

---

## 🚀 Future Improvements

- Multiple strategy comparison
- Parameter optimization
- Machine learning price prediction
- Portfolio diversification simulation
- Deployment to Streamlit Cloud
- Add candlestick charts
- Add live WebSocket streaming

---

## ⚠️ Disclaimer

This project is for educational purposes only.  
It does not provide financial advice or guarantee profits.

---


## 👤 Author

Your Name: Pawan Nikam
Final Year Engineering Student  
Focused on Data Science, Quantitative Analysis & Systems Engineering
