# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	02/12/2024

"""
Day 4: OOP/Classes 

Introduction to Classes with Python
"""


class Person(object):
	"""docstring for Person"""

	def __init__(self,age,height,weight):
		super(Person, self).__init__()
		self.age:int = age
		self.height:int = height #cm
		self.weight:int = weight #Kg
		self.eye_colour: str = ''
		self.hair_colour: str = ''

	def set_age(self): # Return Persons Age
		self.age = age

	def set_height(self,height): # Set Persons heigh
		self.height = height

	def set_weight(self,weight): # Set Persons Weight
		self.weight = weight
	
	def set_eye_colour(self,eye_colour): # Set Persons Weight
		self.eye_colour = eye_colour

	def set_hair_colour(self,hair_colour): # Set Persons Weight
		self.hair_colour = hair_colour 


	def get_age(self): # Return Persons Weight
		return self.age

	def get_height(self): # Return Persons Weight
		return self.height

	def get_weight(self):	# Return Persons Weight
		return self.weight
	
	def get_eye_colour(self): # Return Persons Weight
		return self.eye_colour

	def get_hair_colour(self): # Return Persons Weight
		return self.hair_colour

Person_1 = Person(25,173,90)
print(Person_1.age)
print(Person_1.height)
print(Person_1.weight)
Person_1.set_weight(95)
print(Person_1.weight)
print(Person_1.get_weight())
print(dir(Person))