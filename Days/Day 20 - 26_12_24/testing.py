import pandas as pd

df = pd.read_csv('data.csv')

print(df.info()) 
#print(df)

#df[]
print(df.loc[0])