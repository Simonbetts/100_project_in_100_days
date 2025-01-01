# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	01/01/2024

"""
Day 22: SQLLight - Add data to 

Attempting to seecte data from a csv file to put into the database.

"""

import sqlite3
import pandas as pd

df = pd.read_csv('sales.csv')
connection = sqlite3.connect('company.db')

print(df.info()) 


for x in range(len(df)):

	first_name = df.loc[x, 'first_name']   
	last_name = df.loc[x, 'last_name']  
	email_address = df.loc[x, 'email_address'] 
	number_of_complaints = int(df.loc[x, 'number_of_complaints']) 
	print(f'Data being added: {first_name} {last_name}, {email_address}, {number_of_complaints}')

	data = [
	(first_name,last_name,email_address,number_of_complaints),
	#(first_name,last_name,email,naumbe_of_complaints)
	]

	connection.executemany('INSERT INTO sales() VALUES(?,?,?,?)', data)
	print(f'Data Added!')



# write the data to the file
connection.commit()