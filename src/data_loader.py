import yfinance as yf

def load_stock_data(tickers, start_date, end_date):

    data = yf.download(
        tickers,
        start=start_date,
        end=end_date
    )

    return data