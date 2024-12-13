# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	13/12/2024

"""
Day 14: pandas 
"""

import pandas as pd
print(f'Version: {pd.__version__}\n')

df = pd.read_csv('data.csv')

print(df.to_string()) 
print(f'')
# =====================



mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print(f'')

# ===================
a = [1, 7, 2]

myvar = pd.Series(a,index = ["x", "y", "z"])

print(myvar)
print(myvar["y"])
#print(myvar[0])