## Financial Asset Analysis with Python

# Overview
This project analyzes the historical performance and risk characteristics of multiple financial assets using Python. The analysis combines core finance concepts with data science techniques to study returns, volatility, correlations, and risk-adjusted performance.

Assets analyzed:
- Apple (AAPL)
- Microsoft (MSFT)
- Google (GOOGL)
- SPDR Gold Trust (GLD)
- iShares 20+ Year Treasury Bond ETF (TLT)

---

# Tools & Libraries
- Python
- pandas
- yfinance
- matplotlib

---

# Key Features
- Downloads real historical market data
- Computes daily percentage returns
- Calculates summary statistics
- Computes annualized volatility
- Calculates average returns and Sharpe ratios
- Analyzes asset correlations
- Visualizes financial time series and risk metrics

---

# Visualizations
The project generates the following plots:
- Daily Returns of Assets
- Cumulative Returns (Growth of $1)
- Asset Correlation Heatmap
- 21-Day Rolling Annualized Volatility

---

# Project Structure
finance_project/
│
├── sourcecode/
│ └── main.py
│
├── README.md

---

# How to Run
1. Clone the repository
2. Install required packages: pip install yfinance pandas matplotlib
3. Run the script: python sourcecode/main.py

---

# Key Takeaways
- Technology stocks exhibit higher volatility than bonds and gold
- Equity assets show stronger correlations with each other
- Defensive assets such as bonds and gold provide diversification benefits
- Rolling volatility highlights time-varying risk in financial markets

---

# Future Improvements
- Portfolio optimization and efficient frontier analysis
- Risk-adjusted backtesting strategies
- Macroeconomic regime analysis
- Interactive dashboards

---

# Author
Dhriti  
Rutgers University — Data Science on the Economics Track



