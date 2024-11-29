# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	29/11/2024

"""
Day 1:
A number guessing game. 
- Build a Number guessing game, in which the user selects a range.
- User selected a range from A to B, where A and B belong to Integer.
- Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

# Add a test program?
"""

import random

print(f'------------------------------------------------')
print(f'|------------- Game Started -------------------|')
print(f'------------------------------------------------')
print(f'')
print(f'---------------------------------------------------------')
print(f'| - Your goal is to select a range and number of attmepts|')
print(f'| before guessing what number I select.                  |')
print(f"| - Don't worry, I will help you                         |")
print(f"| - You mut enter integers.                              |")
print(f'---------------------------------------------------------')
print(f'')

upper_limit: int = 0
lower_limit: int = 0
attempt_limit: int = 0
count: int = 0

# Ask User 
print(f'What is the upper limit for guessing')
upper_limit = input()
upper_limit = int(upper_limit)
print(f'What is the lower limit for guessing')
lower_limit = input()
lower_limit = int(lower_limit)
print(f'How many guesses do you get?')
attempt_limit = input()
attempt_limit = int(attempt_limit)
print(f'')

if upper_limit < lower_limit:
	print(f'** The upper limit must be larger so I have swapped your numbers **')
	temp: int = upper_limit
	upper_limit = lower_limit
	lower_limit = temp
	print(f'')


# Game Loop
ans = random.randrange(lower_limit,upper_limit)
answer = int(ans)
guess: int = 0

while count < attempt_limit:

	# Test 
	if count == 0:
		print(f'What is your first guess?')
		guess = input()
	elif count == attempt_limit-1:
		print(f'Last guess? ')
		guess = input()
	else:
		print(f'What is your next guess?')
		guess = input()

	print(f'')

	# Guess Helper
	guess = int(guess)

	if guess == answer:
		print(f'Well done you guessed {guess} and the answer was {answer}!')
		break
	elif guess < answer:
		print(f'You are too low!')
	elif guess > answer:
		print(f'You are too high') 
	else:
		print(f'What....?')
	print(f'')


	# Game Over
	if count == attempt_limit-1:
		print(f'The Answer was: {answer}')
		print(f'GAME OVER - Better luck next time!')
	print(f'')

	count = count + 1

print(f'')
print(f'------------------------------------------------')
print(f'|----------------- Game Over ------------------|')
print(f'------------------------------------------------')
