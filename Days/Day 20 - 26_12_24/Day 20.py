# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	26/12/2024

"""
Day 20: SQLLight - Create the Database



"""

import sqlite3


connection = sqlite3.connect('company.db')

connection.execute('''

	CREATE TABLE IF NOT EXISTS customers(
		customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
		first_name TEXT,
		last_name TEXT,
		email TEXT,
		naumbe_of_complaints INT
		)
	''')

connection.execute('''
	CREATE TABLE IF NOT EXISTS sales(
			purchase_number INTEGER PRIMARY KEY AUTOINCREMENT,
			date_of_purchase DATE,
			customer_id INTEGER,
			item_code INTEGER,

			FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
			FOREIGN KEY (item_code) REFERENCES incantory(item_code)
			)
	''')

connection.execute('''
	CREATE TABLE IF NOT EXISTS invantory(
			item_code INTEGER PRIMARY KEY AUTOINCREMENT,
			item TEXT,
			unit_price_GBP DOUBLE(255,2),
			company_id INTEGER,
			company TEXT,
			sale_phone_number TEXT
			)
	''')




# close the database
connection.close()