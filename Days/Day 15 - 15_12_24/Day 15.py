# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	15/12/2024

"""
Day 15: Panadas

"""

import pandas as pd
print(f'Version: {pd.__version__}\n')

# Intro Pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

dataset = pd.DataFrame(mydataset)

print(dataset)

# Series (one dimensional array)

a = [1, 7, 2]

series = pd.Series(a)

print(f'')
print(series)

# Labels

Labels = pd.Series(a, index = ["x", "y", "z"])

print(f'')
print(f' y = {Labels['y']}')

# Key Object Pairs

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(f'')
print(myvar)

# Data Frames

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(f'')
print(myvar)