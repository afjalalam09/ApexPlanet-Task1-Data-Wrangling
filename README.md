# ApexPlanet Data Analytics Internship - Task 1
**Data Immersion & Wrangling**

**Author:** Afjal Alam

## Objective
The primary goal of this task is to perform data profiling, cleaning, and transformation on a raw sales dataset to make it analysis-ready. This is part of Task 1 for the ApexPlanet Data Analytics Internship.

## Files in this Repository
* `raw_data.csv`: The original, uncleaned dataset containing sales transactions.
* `cleaned_data.csv`: The final, processed dataset ready for Exploratory Data Analysis (EDA).
* `task1.py`: The Python script (using Pandas) written to clean and transform the data.
* `data_dictionary.txt`: A detailed explanation of all columns, their data types, and business relevance.

## Data Cleaning Process
During the data wrangling process, the following issues were addressed using Python (Pandas):
1. **Handling Missing Values:** Filled missing values in the `Postal Code` column.
2. **Standardizing Formats:** Converted `Postal Code` from float to string to remove decimals. Converted `Order Date` and `Ship Date` from text to proper Datetime objects.
3. **Feature Engineering:** Created a new column named `Shipping Days` by calculating the difference between the ship date and the order date to understand delivery timelines.

## How to Run
To replicate the data cleaning process:
1. Ensure Python and the Pandas library are installed.
2. Keep `raw_data.csv` and `task1.py` in the same directory.
3. Run the script in your terminal or IDE.
4. The script will generate the `cleaned_data.csv` file automatically.

## Video Walkthrough
*Link to LinkedIn Video:* (https://lnkd.in/p/gSWsaxFk)
