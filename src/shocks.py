def get_shock_scenario(scenario_name):
    scenarios = {
        "Tech Crash": {
            "AAPL": -0.20,
            "NVDA": -0.30,
            "JPM": -0.05
        },
        "Banking Crisis": {
            "AAPL": -0.05,
            "NVDA": -0.10,
            "JPM": -0.30
        },
        "Full Market Crash": {
            "AAPL": -0.25,
            "NVDA": -0.25,
            "JPM": -0.25
        },
        "AI Bubble Burst": {
            "AAPL": -0.15,
            "NVDA": -0.40,
            "JPM": -0.08
        }
    }

    return scenarios[scenario_name]


def apply_shock(portfolio_values, shock_percentages):
    shocked_values = {}

    for stock, value in portfolio_values.items():
        shock = shock_percentages.get(stock, 0)
        shocked_values[stock] = value * (1 + shock)

    return shocked_values