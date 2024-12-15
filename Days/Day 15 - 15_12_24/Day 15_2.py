# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	15/12/2024

"""
Day 15: Panadas

"""

import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 

# Maximum Rows

# pd.options.display.max_rows = 9999 # Sey number of rows to 9999. Can be used to dispaly more rows. 
print(f'')
print(f'systems maximum rows: {pd.options.display.max_rows}') 

