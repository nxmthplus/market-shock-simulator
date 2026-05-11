def calculate_portfolio_value(total_investment, weights):

    portfolio_values = {}

    for stock, weight in weights.items():

        portfolio_values[stock] = total_investment * weight

    return portfolio_values