# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	06/12/2024

"""
Day 8: SQLite database, inspect and add data. 


"""

import sqlite3

connection = sqlite3.connect('main_database.db')

print(f'=============================')
print(f'=== Please enter the data ===')
print(f'=============================')
print(f'')
 # should be a csv file that can be imported. ask clubs to send excel?
print(f'Please enter the name of the club')
club = input()
#club = "Monmouth"
print(f'Please enter first name')
member_first_name = input()
#member_first_name: str = "Barny"
print(f'Please enter last name')
member_last_name = input()
#member_last_name: str = "Smith"
print(f'Please enter the gender')
member_gender = input()
member_gender: str = "M"
print(f'Is the member on committee, 1=yes, 0=no')
comittee = input()
committee:bool = bool(comittee)
#committee:bool = True
print(f'')

print(f'Please Confirm Details')
print(f'Club: {club}, First Name: {member_first_name}, Last Name: {member_last_name}, Gender:{member_gender},Committee:{committee}')
print(f'Correct = y, incorrect = n')
correct = input()
if correct == 'y':
	print(f'Confirmed Data')
elif correct == 'n':
	print(f'What data is incorrect?')
	## Do a check to se what data is incorrect
else:
	prnt(f'Commands not recognised, pleas eenter y or n (ensure these are lowercase)')
print(f'')

member_data = [
	(club,member_first_name,member_last_name,member_gender,committee)	
]

connection.executemany('INSERT INTO details_database(club,member_first_name,member_last_name,member_gender,committee) VALUES(?,?,?,?,?)', member_data)


# write the data to the file
connection.commit()

# close the database
connection.close()

print(f'Data added to database.')