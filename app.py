import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("Stock Performance Dashboard")

# Load data
df = pd.read_csv("final_stock_data.csv")

returns_df = pd.read_csv("yearly_returns.csv")

# Show dataset
st.subheader("Stock Data")

st.dataframe(df.head())

# Top 10 Green Stocks
top_green = returns_df.sort_values(
    by="Yearly_Return",
    ascending=False
).head(10)

# Chart
st.subheader("Top 10 Green Stocks")

fig, ax = plt.subplots(figsize=(10,5))

ax.bar(
    top_green["Ticker"],
    top_green["Yearly_Return"]
)

plt.xticks(rotation=45)

st.pyplot(fig)

# Top 10 Loss Stocks
top_loss = returns_df.sort_values(
    by="Yearly_Return"
).head(10)

st.subheader("Top 10 Loss Stocks")

fig2, ax2 = plt.subplots(figsize=(10,5))

ax2.bar(
    top_loss["Ticker"],
    top_loss["Yearly_Return"]
)

plt.xticks(rotation=45)

st.pyplot(fig2)

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