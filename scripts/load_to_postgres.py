import pandas as pd
from sqlalchemy import create_engine

# Load cleaned CSV
df = pd.read_csv(r"C:\Users\Mayank\Downloads\fraud-detection-project\data\cleaned_data.csv")
# Convert DOB to proper datetime format (important for SQL)
df['dob'] = pd.to_datetime(df['dob'], errors='coerce')

# Create PostgreSQL engine
engine = create_engine("postgresql://postgres:123456789@localhost:5432/fraud_detection_db")

# Insert into PostgreSQL
df.to_sql("transactions", engine, if_exists="append", index=False)

print("Data successfully inserted into PostgreSQL!")