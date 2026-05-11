def get_sector_shock_scenario(scenario_name):
    scenarios = {
        "Tech Crash": {
            "Technology": -0.30,
            "Communication Services": -0.20,
            "Financial Services": -0.05,
            "Consumer Cyclical": -0.15,
            "Healthcare": -0.05,
            "Consumer Defensive": -0.03,
            "Energy": -0.08,
            "Industrials": -0.10,
            "Unknown": -0.10
        },
        "Banking Crisis": {
            "Financial Services": -0.35,
            "Technology": -0.10,
            "Communication Services": -0.08,
            "Consumer Cyclical": -0.12,
            "Healthcare": -0.05,
            "Consumer Defensive": -0.03,
            "Energy": -0.08,
            "Industrials": -0.12,
            "Unknown": -0.10
        },
        "Full Market Crash": {
            "Technology": -0.25,
            "Financial Services": -0.25,
            "Communication Services": -0.25,
            "Consumer Cyclical": -0.25,
            "Healthcare": -0.15,
            "Consumer Defensive": -0.10,
            "Energy": -0.20,
            "Industrials": -0.25,
            "Unknown": -0.20
        },
        "AI Bubble Burst": {
            "Technology": -0.40,
            "Communication Services": -0.20,
            "Financial Services": -0.08,
            "Consumer Cyclical": -0.15,
            "Healthcare": -0.05,
            "Consumer Defensive": -0.03,
            "Energy": -0.05,
            "Industrials": -0.10,
            "Unknown": -0.12
        },

        "Interest Rate Hike": { 
            "Technology": -0.22,
            "Communication Services": -0.12,
            "Financial Services": 0.05,
            "Consumer Cyclical": -0.15,
            "Healthcare": -0.04,
            "Consumer Defensive": -0.03,
            "Energy": 0.02,
            "Industrials": -0.10,
            "Real Estate": -0.30,
            "Utilities": -0.12,
            "Unknown": -0.10
},
        "Oil Crisis": {
            "Technology": -0.08,
            "Communication Services": -0.07,
            "Financial Services": -0.06,
            "Consumer Cyclical": -0.18,
            "Healthcare": -0.03,
            "Consumer Defensive": -0.05,
            "Energy": 0.20,
            "Industrials": -0.15,
            "Real Estate": -0.08,
            "Utilities": -0.05,
            "Unknown": -0.08    
},
        "Pandemic Shock": {
            "Technology": 0.05,
            "Communication Services": 0.02,
            "Financial Services": -0.18,
            "Consumer Cyclical": -0.25,
            "Healthcare": 0.08,
            "Consumer Defensive": 0.03,
            "Energy": -0.30,
            "Industrials": -0.18,
            "Real Estate": -0.12,
            "Utilities": -0.04,
            "Unknown": -0.10
},
        "AI Boom": {
            "Technology": 0.30,
            "Communication Services": 0.15,
            "Financial Services": 0.03,
            "Consumer Cyclical": 0.08,
            "Healthcare": 0.02,
            "Consumer Defensive": -0.02,
            "Energy": -0.03,
            "Industrials": 0.05,
            "Real Estate": -0.02,
            "Utilities": -0.03,
            "Unknown": 0.05
}
    }

    return scenarios[scenario_name]


def apply_sector_shock(portfolio_values, sector_map, sector_shocks):
    shocked_values = {}

    for stock, value in portfolio_values.items():
        sector = sector_map.get(stock, "Unknown")
        shock = sector_shocks.get(sector, sector_shocks.get("Unknown", -0.10))
        shocked_values[stock] = value * (1 + shock)

    return shocked_values