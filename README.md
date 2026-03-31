🚀 Fintech Data Pipeline (ETL) & SQL Warehouse

📌 Project Overview
This project is a functional Data Engineering Pipeline designed to simulate a fintech user-management system (inspired by the Moniepoint tech stack). It extracts raw user data from a REST API, performs rigorous data cleaning and transformation using Python, and loads the structured data into both a CSV backup and a SQL Relational Database.

''''

🏗️ Tech Stack
Language: Python 3.14

Libraries: Pandas, Requests, SQLAlchemy

Database: SQLite (SQL)

Orchestration Logic: Functional Python ETL Pattern

Concepts: API Integration, Data Quality (Handling Nulls), Data Standardization, and Business Intelligence Reporting.

''''

🛠️ Pipeline Workflow
Extraction (API): * Connects to an external REST API using the requests library.

Implements error handling to ensure pipeline stability if the API is down.

Transformation (Data Cleaning):

Flattening: Unpacks nested JSON objects (Address -> City).

Data Quality: Removes records with missing critical information (Email) using .dropna().

Standardization: Converts location data to uppercase for database indexing consistency.

Feature Engineering: Extracts the email_domain from raw email strings to provide market insights.

Loading (Multi-Destination):

Flat File: Saves a version to cleaned_user_transactions.csv.

Database: Uses SQLAlchemy to load data into a structured SQL table (intern_users) in moniepoint_db.db.

Reporting: * Generates a Business Summary Report directly in the logs, identifying total active users and the primary market (Top City).

''''

📂 File Structure
transaction_pipeline.py: The main ETL script that runs the pipeline.

query_data.py: A SQL analysis script to query the database and generate insights.

moniepoint_db.db: The generated SQL database (Source of Truth).

cleaned_user_transactions.csv: The processed output file.

''''

🚀 How to Run
Install Dependencies:

Bash
pip install pandas requests sqlalchemy
Run the Pipeline:

Bash
python transaction_pipeline.py
Query the Data:

Bash
python query_data.py

''''

📈 Future Roadmap (Phase 3 & 4)
[ ] Containerization: Wrap the pipeline in Docker for consistent deployment.

[ ] Orchestration: Migrate the execution logic to Apache Airflow DAGs.

[ ] Cloud Integration: Automate data loading into Google Cloud Storage (GCS) and BigQuery.

''''

👩‍🏫 Author
Udo Mary | Women Techster Data Science and Engineering Alumi
