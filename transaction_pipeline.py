import requests                                # Library to fetch data from the internet (APIs)
import pandas as pd                            # Library to clean and organize data into tables (DataFrames)
import logging                                 # Library to record what the script is doing

# Setup Logging to show what's happening and when it happens
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# PHASE 1: EXTRACTION
def extract():
    """Fetch user data from the API."""
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)               
        response.raise_for_status() # Check if the website is 'healthy'
        logging.info("Successfully extracted data from API")
        return pd.DataFrame(response.json())
    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        return None

# PHASE 2: TRANSFORMATION (The 'Cleaning' Phase)
def transform(df):
    """Clean the data and flatten the nested address."""
    if df is None: return None
    
    logging.info("Transforming data...")
    # Extracting the city from the nested dictionary
    df["city"] = df["address"].apply(lambda x: x["city"])
    
    # Selecting only needed columns
    df_clean = df[["id", "name", "email", "city"]].copy()
    
    # Standardization: Make city uppercase (Good for database sorting)
    df_clean["city"] = df_clean["city"].str.upper()

    # Data Mining to extract the email domain
    df_clean["email_domain"] = df_clean["email"].str.split('@').str[-1]

    # Removes any rows where the email is missing (null) before you loading
    df_clean = df_clean.dropna(subset=['email'])

    logging.info("Transaction complete. New columns created.")
    return df_clean

# PHASE 3: LOADING
def load(df):
    """Save the final result to a CSV."""
    if df is not None:
        file_name = "cleaned_user_transactions.csv"
        df.to_csv(file_name, index=False)
        logging.info(f"Load complete! Data saved to {file_name}")

def generate_summary_report(df):
    """
    BUSINESS INSIGHT PHASE
    Purpose: Turn raw data into answers for Stakeholders.
    """
    if df is not None and not df.empty:

        # 1. Count the total number of unique IDs
        total_users = len(df)

        # 2. Find the most common city
        top_city = df['city'].value_counts().idxmax()

        logging.info("--- BUSINESS SUMMARY REPORT ---")
        logging.info(f"Total Active Users: {total_users}")
        logging.info(f"Primary Market (Top City): {top_city}")
        logging.info("------------------------------")
    else:
        logging.warning("No data available to generate a report.")

# THE ORCHESTRATOR

if __name__ == "__main__":

    # Step 1: Runs the logic
    raw_data = extract()

    # Step 2: Transforms the results
    clean_data = transform(raw_data)

    # Step 3: Saves to disk
    load(clean_data)

    # Step 4: RUN THE REPORT
    generate_summary_report(clean_data)