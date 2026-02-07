import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "GOOGL", "GLD", "TLT"]

data = yf.download(
    tickers,
    start="2023-01-01",
    end="2024-01-01",
    auto_adjust=True
)

prices = data["Close"]

returns = prices.pct_change()

returns = returns.dropna()

print("First 5 rows of returns:")
print(returns.head())

print("\nSummary statistics:")
print(returns.describe())

plt.figure()
returns.plot(title="Daily Returns of Assets")
plt.xlabel("Date")
plt.ylabel("Daily Return")

volatility = returns.std()

print("\nAnnualized Volatility:")
print(volatility * (252 ** 0.5))

mean_returns = returns.mean()

print("\nAverage Daily Returns:")
print(mean_returns)

sharpe_ratio = mean_returns / returns.std()

print("\nSharpe Ratios:")
print(sharpe_ratio)

correlation = returns.corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.figure()
plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(tickers)), tickers)
plt.yticks(range(len(tickers)), tickers)
plt.title("Asset Correlation Heatmap")

cumulative_returns = (1 + returns).cumprod()

print("\nCumulative returns (first 5 rows):")
print(cumulative_returns.head())

plt.figure()
cumulative_returns.plot(title="Cumulative Returns of Assets")
plt.xlabel("Date")
plt.ylabel("Growth of $1")

rolling_window = 21

rolling_volatility = returns.rolling(window=rolling_window).std()

print("\nRolling volatility (first 5 rows):")
print(rolling_volatility.head())

rolling_vol_annualized = rolling_volatility * (252 ** 0.5)

plt.figure()
rolling_vol_annualized.plot(
    title="21-Day Rolling Annualized Volatility"
)
plt.xlabel("Date")
plt.ylabel("Annualized Volatility")
plt.show()

print("ROLLING VOL CODE RAN")
