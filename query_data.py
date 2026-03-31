import pandas as pd
from sqlalchemy import create_engine
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

# 1. Connect to the database
engine = create_engine('sqlite:///user_transactions_db.db')

def run_analysis(query, description):
    """Helper function to run SQL and print results nicely"""
    logging.info(F"\n--- ANALYSIS: {description} ---")

    # Sends the SQL command to the database to get a DataFrame
    result_df = pd.read_sql(query, con=engine)
    print(result_df)

# SQL Queries - Data Mining

# Query 1: Select all
query_all = "SELECT * FROM users"

# Query 2: Filter by city
query_filter = "SELECT name, email FROM users WHERE city ='BARTHOLOMEBURY'"

# Query 3: Aggregating how many users have each email domain
query_count = """
SELECT email_domain, COUNT(*) as user_count
FROM users
GROUP BY email_domain
ORDER BY user_count DESC
"""

try:
    df = pd.read_sql(query_filter, con=engine)
    if df.empty:
        print("No users found in that city. (Try checking the spelling!)")
    else:
        print(df)
except Exception as e:
    print(f"SQL Error: {e}")

if __name__ == "__main__":
    run_analysis(query_all, "Viewing all recoerds in the Warehouse")
    run_analysis(query_filter, "Filtering for users in a specific city")
    run_analysis(query_count, "Counting users per Email Domain (Market Share)")