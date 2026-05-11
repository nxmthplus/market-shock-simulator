import yfinance as yf
import pandas as pd


def load_stock_data(
    tickers,
    start_date,
    end_date
):

    data = yf.download(
        tickers,
        start=start_date,
        end=end_date
    )["Close"]

    return data


def calculate_daily_returns(data):

    daily_returns = data.pct_change().dropna()

    return daily_returns


def calculate_historical_metrics(daily_returns):

    mean_return = daily_returns.mean().mean()

    volatility = daily_returns.std().mean()

    return mean_return, volatility