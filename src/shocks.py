def apply_shock(portfolio_values, shock_percentages):
    shocked_values = {}

    for stock, value in portfolio_values.items():
        shock = shock_percentages.get(stock, 0)
        shocked_values[stock] = value * (1 + shock)

    return shocked_values