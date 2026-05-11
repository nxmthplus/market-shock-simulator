import streamlit as st
import pandas as pd
import plotly.express as px

from src.portfolio import calculate_portfolio_value
from src.shocks import apply_shock, get_shock_scenario

st.title("Market Shock Simulator")
st.write("Simulate how a portfolio reacts to different market crash scenarios.")

total_investment = st.number_input(
    "Total Investment Amount",
    min_value=1000,
    value=10000,
    step=1000
)

scenario_name = st.selectbox(
    "Choose Shock Scenario",
    ["Tech Crash", "Banking Crisis", "Full Market Crash", "AI Bubble Burst"]
)

st.subheader("Portfolio Weights")

aapl_weight = st.slider("AAPL Weight", 0.0, 1.0, 0.4)
nvda_weight = st.slider("NVDA Weight", 0.0, 1.0, 0.3)
jpm_weight = st.slider("JPM Weight", 0.0, 1.0, 0.3)

weight_values = [aapl_weight, nvda_weight, jpm_weight]
stocks = ["AAPL", "NVDA", "JPM"]

if round(sum(weight_values), 2) != 1.0:
    st.warning("Weights must add up to 1.0")
else:
    weights = dict(zip(stocks, weight_values))

    portfolio_values = calculate_portfolio_value(total_investment, weights)
    shock = get_shock_scenario(scenario_name)
    shocked_values = apply_shock(portfolio_values, shock)

    original_total = sum(portfolio_values.values())
    shocked_total = sum(shocked_values.values())
    loss_amount = original_total - shocked_total
    loss_percentage = loss_amount / original_total * 100

    st.subheader("Results")

    st.metric("Original Portfolio Value", f"${original_total:,.2f}")
    st.metric("Value After Shock", f"${shocked_total:,.2f}")
    st.metric("Loss Amount", f"${loss_amount:,.2f}")
    st.metric("Loss Percentage", f"{loss_percentage:.2f}%")

    df = pd.DataFrame({
        "Original": portfolio_values,
        "After Shock": shocked_values
    })

    st.subheader("Portfolio Value Before vs After Shock")

    plot_df = df.reset_index()
    plot_df.columns = ["Stock", "Original", "After Shock"]

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