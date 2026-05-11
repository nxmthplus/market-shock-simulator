from src.portfolio import calculate_portfolio_value
import matplotlib.pyplot as plt

total_investment = 10000

stocks = ["AAPL", "NVDA", "JPM"]
weight_values = [0.4, 0.3, 0.3]

if sum(weight_values) != 1.0:
    print("Weights must add up to 1.0")
    exit()
    
weights = dict(zip(stocks, weight_values))

portfolio_values = calculate_portfolio_value(
    total_investment,
    weights
)

print(portfolio_values)

labels = portfolio_values.keys()
sizes = portfolio_values.values()

plt.figure(figsize=(8, 8))

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Portfolio Allocation")

plt.show()