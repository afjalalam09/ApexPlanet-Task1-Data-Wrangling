import pandas as pd

# 1. Load the raw dataset
df = pd.read_csv(r'C:\Users\user\Desktop\apexPlanet rask 1\raw_data.csv')

# 2. Handle missing values in the 'Postal Code' column by filling them with 0
df['Postal Code'] = df['Postal Code'].fillna(0)

# 3. Standardize the data type of 'Postal Code' to remove decimals
df['Postal Code'] = df['Postal Code'].astype(int).astype(str)

# 4. Convert date columns from string to proper datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')

# 5. Feature Engineering: Create a new column to calculate total shipping days
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# 6. Save the cleaned and analysis-ready dataset to a new CSV file
df.to_csv(r'C:\Users\user\Desktop\apexPlanet rask 1\cleaned_data.csv', index=False)

print("Data successfully cleaned and saved as 'cleaned_data.csv'")