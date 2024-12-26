# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	26/12/2024

"""
Day 20: SQLLight - Add data to 

Attempting to seecte data from a csv file to put into the database.

"""

import sqlite3
import pandas as pd

df = pd.read_csv('customers.csv')
connection = sqlite3.connect('company.db')

print(df.info()) 

old_data = []
frame = (4)
#print(df)
print(f'## Here ##\n')
#print(df.loc[[0],[1]])
print(df.loc[[0,2,5]])
print(f'')
print(df.iloc[[0,1]])

#Dataframe.loc[["row1"], ["column1"]]


# Insert data into the table
data = [
	("Example","Example","example@example.com",0),
	#(first_name,last_name,email,naumbe_of_complaints)

]


connection.executemany('INSERT INTO customers(first_name,last_name,email,naumbe_of_complaints) VALUES(?,?,?,?)', data)


# write the data to the file
connection.commit()