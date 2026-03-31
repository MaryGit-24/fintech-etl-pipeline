import requests                                # Library to fetch data from the internet (APIs)
import pandas as pd                            # Library to clean and organize data into tables (DataFrames)
import logging                                 # Library to record what the script is doing
from sqlalchemy import create_engine           # Tool to connect to databases

# Setup Logging to show what's happening and when it happens
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# PHASE 1: EXTRACTION

def extract():
    """Fetch user data from the API."""
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)

        # Check if the website is 'healthy'               
        response.raise_for_status()
        logging.info("Extraction Success: Data pulled from API.")
        return pd.DataFrame(response.json())
    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        return None

# PHASE 2: TRANSFORMATION (The 'Cleaning' Phase)

def transform(df):

    """Clean and prepare the data."""
    if df is None: return None
    logging.info("Transforming: Standardizing city and email domains...")

    # Flattening the nested address to get the city
    df["city"] = df["address"].apply(lambda x: x["city"])
    
    # Selecting columns and making a clean copy
    df_clean = df[["id", "name", "email", "city"]].copy()
    
    # Standardization text
    df_clean["city"] = df_clean["city"].str.upper()

    # Engineering a new feature: Email Domain
    df_clean["email_domain"] = df_clean["email"].str.split('@').str[-1]

    # Removes any rows where the email is missing (null) before you loading
    df.dropna(subset=['email'])

    return df_clean

# PHASE 3: THE TWO LOAD FUNCTIONS

def load_to_csv(df):
    """Save a local backup file."""
    if df is not None:
        df.to_csv("user_transactions_backup.csv", index=False)
        logging.info("Load Success: CSV file created.")
        
def load_to_sql(df):
    """Save to a Relational Database (SQL)."""
    if df is not None:
        
        # Create a local SQLite database file named 'user_transactions_db.db'
        engine = create_engine('sqlite:///user_transactions_db.db')

        # Write the data into a table called 'users'
        df.to_sql('users', con=engine, if_exists='replace', index=False)

        logging.info("SQL Load Success: Data written to 'user_transactions_db.db'.")

# THE ORCHESTRATOR
if __name__ == "__main__":
    logging.info("PIPELINE STARTED")

    # 1. Extract
    raw_df = extract()

    # 2. Transform
    clean_df = transform(raw_df)

    # 3. Load (To CSV for backup AND to SQL for the Warehouse)
    load_to_csv(clean_df)        # CSV Version
    load_to_sql(clean_df)        # SQL Version

    logging.info("PIPELINE FINISHED SUCCESFULLY")