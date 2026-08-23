import pandas as pd
import numpy as np

# 1. Data Access & Familiarization
print("Loading data...")
df = pd.read_csv("raw_data.csv")

# 2. Data Quality Assessment (Initial Profiling)
print("\n--- Initial Data Profiling ---")
print("Missing values before cleaning:\n", df.isnull().sum())
print("Total duplicate rows:", df.duplicated().sum())

# 3. Data Cleaning & Transformation

# A. Remove Duplicates
df = df.drop_duplicates()

# B. Handle Missing Values
if 'Sales' in df.columns:
    # Fill missing values in numeric columns with the median
    df['Sales'] = df['Sales'].fillna(df['Sales'].median())

if 'Segment' in df.columns:
    # Fill missing categorical/text values with 'Unknown'
    df['Segment'] = df['Segment'].fillna('Unknown')

# C. Fix Inconsistent Formatting (Text Cleaning)
if 'Customer_Name' in df.columns:
    # Remove extra spaces and convert text to Title Case
    df['Customer_Name'] = df['Customer_Name'].str.strip().str.title()

# D. Standardize Date Formats & Feature Engineering
if 'Order_Date' in df.columns:
    # Standardize the date format to datetime objects
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
    
    # Feature Engineering: Extract Year and Month into new columns
    df['Order_Year'] = df['Order_Date'].dt.year
    df['Order_Month'] = df['Order_Date'].dt.month_name()

# E. Handling Outliers (Example for Sales)
if 'Sales' in df.columns:
    # Cap outliers at the 99th percentile to prevent skewing analysis
    upper_limit = df['Sales'].quantile(0.99)
    df.loc[df['Sales'] > upper_limit, 'Sales'] = upper_limit

# 4. Save Final Analysis-Ready Dataset
df.to_csv("cleaned_data.csv", index=False)
print("\nData cleaning complete! Cleaned dataset saved as 'cleaned_data.csv'.")