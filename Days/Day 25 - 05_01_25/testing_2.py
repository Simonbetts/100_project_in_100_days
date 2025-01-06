import random

class trooper(object):
	"""docstring for trooper"""
	def __init__(self):
		super(trooper, self).__init__()
		self.hp:int = 100
		self.attack:int = 100
		self.deffence:int = 100

	def attack(other):
		self.attack = self.attack*random()
		print(f'Attack = {self.attack}')
		deffence = other*random()
		print(f'Attack = {other.deffence}')

		if self.attack > other.deffence:
			other.hp = other.hp - (self.attack - other.deffence)


def main():
	trooper_1 = trooper()
	trooper_2 = trooper()

	trooper_1.attack(trooper_2.deffence)
		
if __name__ == '__main__':
	main()