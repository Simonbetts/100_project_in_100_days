# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	06/12/2024

"""
Day 8: SQLite database, inspect and add data. 


"""

import sqlite3 

# Connecting to sqlite 

connection = sqlite3.connect('main_database.db')

# Query data from database
result = connection.execute('SELECT id,member_first_name,member_last_name,committee FROM details_database') # * is wildcard, returns all data from database. Note: Bad practice.
data = result.fetchall()

# disply the data
for row in data:
		print(f'ID: {row[0]}')
		print(f'First Name: {row[1]}')
		print(f'Last Name: {row[2]}')

		if row[3] == 1:
			print(f'Committee: Yes')
		elif row[3] == 0:
			print(f'Committee: No')
		
		print(f'')





# write the data to the file
connection.commit()

# close the database
connection.close()
