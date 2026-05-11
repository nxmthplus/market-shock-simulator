from src.sector_mapper import get_sector_map
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from src.simulation import (
    run_monte_carlo_simulation,
    get_monte_carlo_parameters
)

from src.portfolio import calculate_portfolio_value
from src.shocks import get_sector_shock_scenario, apply_sector_shock
from src.data_loader import (
    load_stock_data,
    calculate_daily_returns,
    calculate_historical_metrics
)


st.title("Market Shock Simulator")

st.write(
    "Simulate how a portfolio reacts to different market crash scenarios."
)

total_investment = st.number_input(
    "Total Investment Amount",
    min_value=1000,
    value=10000,
    step=1000
)

scenario_name = st.selectbox(
    "Choose Shock Scenario",
    [
        "Tech Crash",
        "Banking Crisis",
        "Full Market Crash",
        "AI Bubble Burst",
        "Interest Rate Hike",
        "Oil Crisis",
        "Pandemic Shock",
        "AI Boom"
    ]

    
)

scenario_descriptions = {
    "Tech Crash": "Simulates a selloff in high-growth technology stocks, based on the 2022 tech market downturn.",
    "Banking Crisis": "Simulates financial-sector stress using historical crisis-period market behavior.",
    "Full Market Crash": "Simulates a broad market selloff where most assets are under pressure.",
    "AI Bubble Burst": "Simulates a sharp correction in AI-related growth stocks.",
    "Interest Rate Hike": "Simulates aggressive central bank rate hikes, hurting growth stocks and rate-sensitive sectors.",
    "Oil Crisis": "Simulates a sharp rise in oil prices, benefiting energy stocks while pressuring consumers and industrial firms.",
    "Pandemic Shock": "Simulates pandemic-style disruption where healthcare and tech may hold up better than travel, energy, and cyclicals.",
    "AI Boom": "Simulates a positive AI-driven rally, especially benefiting technology and communication services stocks."
}

st.info(scenario_descriptions[scenario_name])

st.subheader("Portfolio Weights")

popular_stocks = pd.DataFrame({
    "Company": [
        "Apple",
        "Microsoft",
        "Nvidia",
        "Amazon",
        "Alphabet / Google",
        "Meta Platforms",
        "Tesla",
        "JPMorgan Chase",
        "Berkshire Hathaway",
        "Eli Lilly",
        "Broadcom",
        "Visa",
        "Mastercard",
        "Exxon Mobil",
        "UnitedHealth",
        "Walmart",
        "Procter & Gamble",
        "Johnson & Johnson",
        "Netflix",
        "Advanced Micro Devices"
    ],
    "Ticker": [
        "AAPL",
        "MSFT",
        "NVDA",
        "AMZN",
        "GOOGL",
        "META",
        "TSLA",
        "JPM",
        "BRK-B",
        "LLY",
        "AVGO",
        "V",
        "MA",
        "XOM",
        "UNH",
        "WMT",
        "PG",
        "JNJ",
        "NFLX",
        "AMD"
    ]
})

with st.expander("Popular stock ticker guide"):
    st.dataframe(popular_stocks)

    st.markdown(
    "[View full Yahoo Finance ticker list](https://finance.yahoo.com/markets/stocks/)"
    )

ticker_input = st.text_input(
    "Enter stock tickers separated by commas",
    "AAPL,NVDA,JPM,MSFT,GOOGL"
)


stocks = [
    ticker.strip().upper()
    for ticker in ticker_input.split(",")
    if ticker.strip() != ""
]

weight_values = []

for stock in stocks:
    weight = st.slider(
        f"{stock} Weight",
        0.0,
        1.0,
        round(1.0 / len(stocks), 2)
    )
    weight_values.append(weight)

if round(sum(weight_values), 2) != 1.0:

    st.warning("Weights must add up to 1.0")

else:

    weights = dict(zip(stocks, weight_values))

    portfolio_values = calculate_portfolio_value(
        total_investment,
        weights
    )

    sector_map = get_sector_map(stocks)
    sector_shocks = get_sector_shock_scenario(
        scenario_name
    )

    shocked_values = apply_sector_shock(
        portfolio_values,
        sector_map,
        sector_shocks

    )

    original_total = sum(portfolio_values.values())
    shocked_total = sum(shocked_values.values())

    loss_amount = original_total - shocked_total

    loss_percentage = (
        loss_amount / original_total
    ) * 100

    st.subheader("Results")

    st.metric(
        "Original Portfolio Value",
        f"${original_total:,.2f}"
    )

    st.metric(
        "Value After Shock",
        f"${shocked_total:,.2f}"
    )

    st.metric(
        "Loss Amount",
        f"${loss_amount:,.2f}"
    )

    st.metric(
        "Loss Percentage",
        f"{loss_percentage:.2f}%"
    )

    df = pd.DataFrame({
        "Original": portfolio_values,
        "After Shock": shocked_values
    })

    st.subheader(
        "Portfolio Value Before vs After Shock"
    )

    plot_df = df.reset_index()

    plot_df.columns = [
        "Stock",
        "Original",
        "After Shock"
    ]

    fig = px.bar(
        plot_df,
        x="Stock",
        y=["Original", "After Shock"],
        barmode="group",
        title="Portfolio Value Comparison"
    )

    st.plotly_chart(fig)

    st.subheader("Portfolio Allocation")

    allocation_df = pd.DataFrame({
        "Stock": stocks,
        "Weight": weight_values
    })

    st.dataframe(allocation_df)
    historical_periods = {
        "Tech Crash": ("2022-01-01", "2022-12-31"),
        "Banking Crisis": ("2008-01-01", "2008-12-31"),
        "Full Market Crash": ("2020-02-01", "2020-04-30"),
        "AI Bubble Burst": ("2022-01-01", "2022-12-31"),
        "Interest Rate Hike": ("2022-01-01", "2022-12-31"),
        "Oil Crisis": ("2022-02-01", "2022-06-30"),
        "Pandemic Shock": ("2020-02-01", "2020-04-30"),
        "AI Boom": ("2023-01-01", "2023-12-31")
    }

    start_date, end_date = historical_periods[scenario_name]

    historical_data = load_stock_data(
        stocks,
        start_date,
        end_date
    )

    daily_returns = calculate_daily_returns(
        historical_data
    )

    expected_return, volatility = (
        calculate_historical_metrics(
            daily_returns
        )
    )

    st.subheader("Monte Carlo Risk Simulation")

    num_simulations = st.slider(
        "Number of Simulations",
        min_value=100,
        max_value=5000,
        value=1000,
        step=100
    )


    st.write(
        f"Scenario Expected Return: "
        f"{expected_return * 100:.1f}%"
    )

    st.write(
        f"Scenario Volatility: "
        f"{volatility * 100:.1f}%"
    )

    simulation_results = run_monte_carlo_simulation(
        shocked_total,
        expected_return,
        volatility,
        num_simulations
    )

    average_value = (
        sum(simulation_results)
        / len(simulation_results)
    )

    worst_case = np.percentile(simulation_results, 5)

    best_case = max(simulation_results)

    st.metric(
        "Average Simulated Value",
        f"${average_value:,.2f}"
    )

    st.metric(
        "Worst Simulated Value",
        f"${worst_case:,.2f}"
    )

    st.metric(
        "Best Post-Shock Simulated Value",
        f"${best_case:,.2f}"
    )

    simulation_df = pd.DataFrame({
        "Final Portfolio Value": simulation_results
    })

    fig_sim = px.histogram(
        simulation_df,
        x="Final Portfolio Value",
        nbins=50,
        title=(
            "Distribution of Simulated "
            "Portfolio Outcomes"
        )
    )

    st.plotly_chart(fig_sim)