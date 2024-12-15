# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	15/12/2024

"""
Day 15: Panadas (Analyzing Data)

"""

import pandas as pd

dataframe = pd.read_csv('puls_data.csv')

print(dataframe.head()) # Headers and top 5 rows; head(10) would give 10 rows.
print(f'')

print(dataframe.tail()) # Headers and bottom 5 rows
print(f'')

print(dataframe.info()) # Print information about the data
print(f'')

# ======================= CLEAN DATA ======================= #

"""
Data cleaning means fixing bad data in your data set.

Bad data could be:

- Empty cells
- Data in wrong format
- Wrong data
- Duplicates

cals_data.csv has the following:
* The data set contains some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).
* The data set contains wrong format ("Date" in row 26).
* The data set contains wrong data ("Duration" in row 7).
* The data set contains duplicates (row 11 and 12).
"""

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

new_df = dataframe.dropna()
print(new_df.to_string())
print(f'')

# Note: If you want to change the original DataFrame, use the inplace = True argument

#dataframe.dropna(inplace = True) # Remove all rows with NULL values
#dataframe.fillna(130, inplace = True) # Replace NULL values with the number 130
#dataframe["Calories"].fillna(130.0, inplace = True) # Replace NULL values in the "Calories" columns with the number 130
#print(dataframe.to_string())
print(f'')
print(dataframe.info())
print(f'')

# A possibly better method

#x = dataframe["Calories"].mean()

#x = dataframe.mean({"Calories", inplace = True})
#print(x)
#dataframe["Calories"].fillna(x, inplace = True) 