# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	06/12/2024

"""
Day 8: SQLite database, inspect and add data. 


"""

import sqlite3

connection = sqlite3.connect('main_database.db')

connection.execute('''

	CREATE TABLE IF NOT EXISTS main_database(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			club_name Text NOT NULL,
			bsac_number INTEGER,
			club_night Char(9),
			number_of_members INTEGER,
			club_chair Char(25),
			club_sec Char(25),
			club_tres Char(25),
			club_diving_off	Char(25)
			)
	''')

connection.execute('''

	CREATE TABLE IF NOT EXISTS details_database(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			club Char(25),
			member_first_name Char(25) NOT NULL,
			member_last_name Char(25) NOT NULL,
			member_gender Char(25),
			committee BOOL,
			FOREIGN KEY(club) REFERENCES main_database(club_name)
			)
	''')

# Insert data into the table
initial_data = [
	("Monmouth Club",300,"Wednesday",7),
	("Chepstow Club",301,"Wednesday",13),
	("Ross on Wye Club",302,"Friday",10)
]

member_data = [
	("Monmouth","Simon","Smith","Male",0)
	
]

connection.executemany('INSERT INTO main_database(club_name,bsac_number,club_night,number_of_members) VALUES(?,?,?,?)', initial_data)
connection.executemany('INSERT INTO details_database(club,member_first_name,member_last_name,member_gender,committee) VALUES(?,?,?,?,?)', member_data)


# write the data to the file
connection.commit()

# close the database
connection.close()

print(f'Database has been created')