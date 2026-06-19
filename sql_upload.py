import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv("final_stock_data.csv")

# Create MySQL connection
engine = create_engine(
    "mysql+pymysql://root:@localhost/stock_market_db"
)

# Upload dataframe to MySQL
df.to_sql(
    name="stock_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data uploaded successfully")