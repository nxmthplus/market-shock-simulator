import yfinance as yf


def get_stock_sector(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return info.get("sector", "Unknown")
    except Exception:
        return "Unknown"


def get_sector_map(tickers):
    sector_map = {}

    for ticker in tickers:
        sector_map[ticker] = get_stock_sector(ticker)

    return sector_map