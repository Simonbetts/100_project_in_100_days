# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	03/12/2024

"""
Day 5: Keyboard Control 

Use keyboard to move a player around a map.
"""

import keyboard
from time import sleep


print(f'Program Started')

while True:
	if keyboard.is_pressed('w'):
		print(f'Going up')
		sleep(0.5)
	elif keyboard.is_pressed('s'):
		print(f'Going down')
		sleep(0.5)
	elif keyboard.is_pressed('a'):
		print(f'Going left')
		sleep(0.5)
	elif keyboard.is_pressed('d'):
		print(f'Going right')
		sleep(0.5)
	elif keyboard.is_pressed('q'):
		break
	continue

print(f'Program Ended')