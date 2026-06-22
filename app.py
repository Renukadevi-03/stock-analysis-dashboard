import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Page title
st.title("Stock Performance Dashboard")

# Load data
df = pd.read_csv("final_stock_data.csv")

returns_df = pd.read_csv("yearly_returns.csv")

# Top 10 Volatile stocks
volatility_df = pd.read_csv(
    "volatility_data.csv"
)

st.subheader("Top Volatile Stocks")

top_vol = volatility_df.sort_values(
    by="Volatility",
    ascending=False
).head(10)

fig3, ax3 = plt.subplots(figsize=(10,5))

ax3.bar(
    top_vol["Ticker"],
    top_vol["Volatility"]
)

plt.xticks(rotation=45)

st.pyplot(fig3)

# Sector Performances
sector_df = pd.read_csv(
    "sector_performance.csv"
)

st.subheader("Sector Performance")

fig4, ax4 = plt.subplots(
    figsize=(10,5)
)

ax4.bar(
    sector_df["sector"],
    sector_df["Yearly_Return"]
)

plt.xticks(rotation=45)

st.pyplot(fig4)

# Correlation Heatmap
st.subheader(
    "Correlation Heatmap"
)

st.image(
    "correlation_heatmap.png"
)

# Monthly Analysis
monthly_df = pd.read_csv(
    "monthly_returns.csv"
)

st.subheader(
    "Monthly Top 5 Gainers and Losers"
)

selected_month = st.selectbox(
    "Select Month",
    sorted(monthly_df["Month"].unique())
)

month_data = monthly_df[
    monthly_df["Month"] == selected_month
]

top_gainers = month_data.sort_values(
    by="Monthly_Return",
    ascending=False
).head(5)

top_losers = month_data.sort_values(
    by="Monthly_Return"
).head(5)

col1, col2 = st.columns(2)

with col1:

    st.write("Top 5 Gainers")

    fig5, ax5 = plt.subplots(
        figsize=(6,4)
    )

    ax5.bar(
        top_gainers["Ticker"],
        top_gainers["Monthly_Return"]
    )

    plt.xticks(rotation=45)

    st.pyplot(fig5)

with col2:

    st.write("Top 5 Losers")

    fig6, ax6 = plt.subplots(
        figsize=(6,4)
    )

    ax6.bar(
        top_losers["Ticker"],
        top_losers["Monthly_Return"]
    )

    plt.xticks(rotation=45)

    st.pyplot(fig6)

    # Cumulative Return Analysis

st.subheader(
    "Cumulative Return - Top 5 Performing Stocks"
)

cum_df = pd.read_csv(
    "final_stock_data.csv"
)

# Convert Date
cum_df["Date"] = pd.to_datetime(
    cum_df["Date"]
)

# Sort data
cum_df = cum_df.sort_values(
    by=["Ticker", "Date"]
)

# Calculate Daily Return
cum_df["Daily_Return"] = (
    cum_df.groupby("Ticker")["Close"]
    .pct_change()
)

# Calculate Cumulative Return
cum_df["Cumulative_Return"] = (
    1 + cum_df["Daily_Return"]
)

cum_df["Cumulative_Return"] = (
    cum_df.groupby("Ticker")
    ["Cumulative_Return"]
    .cumprod()
)

# Find Top 5 Performing Stocks
top5 = returns_df.sort_values(
    by="Yearly_Return",
    ascending=False
).head(5)

top5_tickers = top5["Ticker"].tolist()

# Plot
fig7, ax7 = plt.subplots(
    figsize=(12,6)
)

for ticker in top5_tickers:

    stock = cum_df[
        cum_df["Ticker"] == ticker
    ]

    ax7.plot(
        stock["Date"],
        stock["Cumulative_Return"],
        label=ticker
    )

ax7.set_title(
    "Top 5 Stocks by Cumulative Return"
)

ax7.set_xlabel("Date")

ax7.set_ylabel(
    "Cumulative Return"
)

ax7.legend()

plt.xticks(rotation=45)

st.pyplot(fig7)