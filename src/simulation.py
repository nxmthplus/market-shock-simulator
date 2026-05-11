import numpy as np


def get_monte_carlo_parameters(scenario_name):
    parameters = {
        "Tech Crash": {
            "expected_return": -0.08,
            "volatility": 0.35
        },
        "Banking Crisis": {
            "expected_return": -0.12,
            "volatility": 0.45
        },
        "Full Market Crash": {
            "expected_return": -0.20,
            "volatility": 0.60
        },
        "AI Bubble Burst": {
            "expected_return": -0.10,
            "volatility": 0.50
        }
    }

    return parameters[scenario_name]


def run_monte_carlo_simulation(
    total_investment,
    expected_return,
    volatility,
    num_simulations
):
    final_values = []

    for _ in range(num_simulations):
        random_return = np.random.normal(expected_return, volatility)
        final_value = total_investment * (1 + random_return)

        # Prevent impossible negative portfolio values
        final_value = max(final_value, 0)

        final_values.append(final_value)

    return final_values