import yfinance as yf
import pandas as pd


def load_stock_data(tickers, start_date, end_date):
    data = yf.download(
        tickers,
        start=start_date,
        end=end_date
    )["Close"]

    return data


def calculate_daily_returns(data):
    # Remove stocks with no data at all
    data = data.dropna(axis=1, how="all")

    # Remove remaining rows with missing values
    data = data.dropna()

    if data.empty:
        return pd.DataFrame()

    daily_returns = data.pct_change().dropna()

    return daily_returns


def calculate_historical_metrics(daily_returns):
    if daily_returns.empty:
        return -0.05, 0.25

    mean_return = daily_returns.mean().mean()
    volatility = daily_returns.std().mean()

    if pd.isna(mean_return):
        mean_return = -0.05

    if pd.isna(volatility):
        volatility = 0.25

    return mean_return, volatility