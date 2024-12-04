# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	30/11/2024

"""
Day 2: Dice Simultor 
- Change between differnt dies on dive
- rolls the dice and give a respnse.
- Created an .exe executable file with python library.
"""

import random

print(f'------------------------------------------------')
print(f'|------------- Game Started -------------------|')
print(f'------------------------------------------------')
print(f'')
print(f'----------------------------------------------------------')
print(f'|                      Dice Simulator                    |')
print(f'|                                                        |')
print(f"| - Select the number of side on your dice               |")
print(f"| - Select the number of dice you are rolling            |")
print(f"| - You mut enter integers.                              |")
print(f'----------------------------------------------------------')
print(f'')

dice_sides: int = 0
number_of_dice: int = 0

print(f'How many sides does your dice have?')
dice_sides = input()
dice_sides = int(dice_sides)
print(f'')

print(f'How dice are you rolling?')
number_of_dice = input()
number_of_dice = int(number_of_dice)
print(f'')



count: int = 0

while count < number_of_dice:

	answer = random.randrange(1,dice_sides)

	
	print(f'Dice {count+1} rolled a {answer}')
	

	count = count +1


print(f'')
print(f'------------------------------------------------')
print(f'|----------------- Game Over ------------------|')
print(f'------------------------------------------------')
k=input("press any key to exit") 