import pandas as pd
import matplotlib.pyplot as plt

from sqlalchemy import create_engine

# MySQL Connection
engine = create_engine(
    "mysql+pymysql://root:@localhost/stock_market_db"
)

# Read data
query = "SELECT * FROM stock_data"

df = pd.read_sql(query, con=engine)

print(df.head())
print(df.info())

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Sort values properly
df.sort_values(
    by=["Ticker", "Date"],
    inplace=True
)

print(df.head())

returns = []

# Loop through each stock ticker
for ticker in df["Ticker"].unique():

    # Filter one stock data
    stock_df = df[df["Ticker"] == ticker]

    # First closing price
    first_close = stock_df.iloc[0]["Close"]

    # Last closing price
    last_close = stock_df.iloc[-1]["Close"]

    # Calculate yearly return
    yearly_return = (
        (last_close - first_close)
        / first_close
    ) * 100

    # Store result
    returns.append([
        ticker,
        yearly_return
    ])

# Create new dataframe
returns_df = pd.DataFrame(
    returns,
    columns=["Ticker", "Yearly_Return"]
)

print(returns_df.head())

# Top 10 Green Stocks
top_green = returns_df.sort_values(
    by="Yearly_Return",
    ascending=False
).head(10)

print("\nTop 10 Green Stocks\n")

print(top_green)

# Top 10 Red Stocks
top_red = returns_df.sort_values(
    by="Yearly_Return"
).head(10)

print("\nTop 10 Red Stocks\n")

print(top_red)

# Green Stocks Count
green_count = (
    returns_df["Yearly_Return"] > 0
).sum()

# Red Stocks Count
red_count = (
    returns_df["Yearly_Return"] < 0
).sum()

# Average Closing Price
average_price = df["Close"].mean()

# Average Volume
average_volume = df["Volume"].mean()

print("\nMarket Summary\n")

print("Green Stocks :", green_count)

print("Red Stocks :", red_count)

print("Average Closing Price :", round(average_price, 2))

print("Average Volume :", round(average_volume, 2))

# Calculate Daily Return
df["Daily_Return"] = (
    df.groupby("Ticker")["Close"]
    .pct_change()
)

print(df.head())

# Volatility Calculation
volatility_df = (
    df.groupby("Ticker")["Daily_Return"]
    .std()
    .reset_index()
)

# Rename column
volatility_df.rename(
    columns={
        "Daily_Return": "Volatility"
    },
    inplace=True
)

print(volatility_df.head())

top_volatile = volatility_df.sort_values(
    by="Volatility",
    ascending=False
).head(10)

print("\nTop 10 Most Volatile Stocks\n")

print(top_volatile)

# Volatility Bar Chart

plt.figure(figsize=(12,6))

plt.bar(
    top_volatile["Ticker"],
    top_volatile["Volatility"]
)

plt.title("Top 10 Most Volatile Stocks")

plt.xlabel("Ticker")

plt.ylabel("Volatility")

plt.xticks(rotation=45)

plt.show()