from src.portfolio import calculate_portfolio_value
from src.shocks import apply_shock, get_shock_scenario
import matplotlib.pyplot as plt
import pandas as pd

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

from src.shocks import apply_shock, get_shock_scenario

scenario_name = "AI Bubble Burst"

shock = get_shock_scenario(scenario_name)

shocked_values = apply_shock(portfolio_values, shock)

original_total = sum(portfolio_values.values())
shocked_total = sum(shocked_values.values())
loss_amount = original_total - shocked_total
loss_percentage = loss_amount / original_total * 100

print("Scenario:", scenario_name)
print("Original portfolio:", portfolio_values)
print("After shock:", shocked_values)
print("Original total:", original_total)
print("After shock total:", shocked_total)
print("Loss amount:", loss_amount)
print("Loss percentage:", round(loss_percentage, 2), "%")

df = pd.DataFrame({
    "Original": portfolio_values,
    "After Shock": shocked_values
})

df.plot(kind="bar", figsize=(10, 6))

plt.title("Portfolio Value Before and After Market Shock")
plt.xlabel("Stock")
plt.ylabel("Value")
plt.xticks(rotation=0)
plt.grid(axis="y")

plt.show()