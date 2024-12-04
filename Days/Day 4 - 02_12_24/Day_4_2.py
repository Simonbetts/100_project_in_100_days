# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	02/12/2024

"""
Day 4.2: OOP/Classes 

Use the classes to make player. The players can go around a map.
The goal is to find the missing person.

# upgade - have player input the details of missing person.
"""

import sys
import keyboard
from time import sleep

keyboard_delay:float = 0.1

class Player(object):
	"""docstring for Player"""

	def __init__(self,name,height,):
		super(Player, self).__init__()
		self.location_x:int = 0
		self.location_y:int = 0
		self.name:str = name
		self.height:int = height #cm #Height results in search radius?

	def view(self):
		top_x:int = self.location_x+5
		bottom_x:int = self.location_x-5
		top_y:int = self.location_y+5
		bottom_y:int = self.location_y-5
		print(f'x view {top_x},{bottom_x}')
		print(f'y view {top_y},{bottom_y}')

	def set_name(self): # Return Persons Age
		self.age = age
	def set_heigt(self,height): # Set Persons heigh
		self.height = height
	def set_location(self,move_by_x,move_by_y):
		self.location_x = self.location_x + move_by_x
		self.location_y = self.location_y + move_by_y

	def get_name(self): # Return Persons name
		return self.name
	def get_height(self): # Return Persons Weight
		return self.height
	def get_location(self):
		return self.location_x, self.location_y

	


def main():

	map_x_length:int = 100
	map_y_length:int = 100

	hidden_player = Player('John',173)
	hidden_player.set_location(18,30)
	hidden_player.get_location()

	searcher_player = Player('Andy',173)

	#if hidden_player is in search_player view area then found end search. 

	print(f'Welcome Player')
	print(f'')
	print(f'You have been Spawned at Location: ')
	print(searcher_player.get_location())

	running = 0

	while running<100:

		
		print('Move using W,A,S,D keys. Quit using Q')
		
		if searcher_player.location_x<map_x_length and searcher_player.location_y<map_y_length:
			
			if keyboard.is_pressed('w'):
				print(f'Going up')
				searcher_player.set_location(5,0)
				sleep(keyboard_delay)
			elif keyboard.is_pressed('s'):
				searcher_player.set_location(-5,0)
				sleep(keyboard_delay)
			elif keyboard.is_pressed('a'):
				print(f'Going left')
				searcher_player.set_location(0,-5)
				sleep(keyboard_delay)
			elif keyboard.is_pressed('d'):
				print(f'Going right')
				searcher_player.set_location(0,5)
				sleep(keyboard_delay)
			elif keyboard.is_pressed('q'):
				break

		else:
			print('You have hit the boundry of the map.')

		# see = player postiion -x to x and -y to y
		print(searcher_player.get_location())
		print(f'')
		
		# running = False
		sleep(0.5)
		running = running +1


if __name__ == '__main__':
	try:
		main()
	finally:
		print("Game Over")

