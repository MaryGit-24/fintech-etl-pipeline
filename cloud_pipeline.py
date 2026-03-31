import pandas as pd
import logging
from google.cloud import storage        # The official Google Cloud Storage library
import os                               # To handle file paths

# 1. Setup Logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """
    SIMULATION: Uploads a file to a Google Cloud Storage bucket.
    """
    try:
        # Step A: Initialize the Storage Client
        storage_client = storage.Client()

        # Step B: Get the bucket object
        bucket = storage_client.bucket(bucket_name)

        # Step C: Create a 'blob' (Google's word for a file in the cloud)
        blob = bucket.blob(destination_blob_name)

        # Step D: Upload the file
        blob.upload_from_filename(source_file_name)

        logging.info(f"SIMULATION: File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}.")

    except Exception as e:
        logging.error(f"Cloud Upload Failed: {e}")

if __name__ == "__main__":

    # Settings for simulation
    MY_BUCKET = "user-transactions-bucket"
    LOCAL_FILE = "user_processed_data.csv"
    CLOUD_NAME = "uploads/daily_users.csv"

    logging.info("--- STARTING CLOUD SIMULATION ---")

    # Call the upload function
    upload_to_gcs(MY_BUCKET, LOCAL_FILE, CLOUD_NAME)