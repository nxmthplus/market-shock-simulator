from src.data_loader import load_stock_data
import matplotlib.pyplot as plt

data = load_stock_data(
    ["AAPL", "NVDA"],
    "2024-01-01",
    "2025-01-01"
)

close_prices = data["Close"]

close_prices.plot(figsize=(12, 6))

plt.title("Stock Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)

plt.show()