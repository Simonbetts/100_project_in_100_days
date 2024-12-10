# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	10/12/2024

"""
Day 11: Turtles
https://docs.python.org/3/library/turtle.html
https://realpython.com/beginners-guide-python-turtle/
"""

import turtle as t
from random import random

#for i in range(100):
#    steps = int(random() * 100)
#    angle = int(random() * 360)
#    print(f'Steps: {steps}')
#    print(f'Angle: {angle}')
#    t.right(angle)
#    t.fd(steps)
steps = 100
angle = 90

for i in range(4):
	
	print(f'Steps: {steps}')
	print(f'Angle: {angle}')
	t.right(angle)
	t.fd(steps)

for i in range(4):
	
	print(f'Steps: {steps}')
	print(f'Angle: {angle}')
	t.circle(60)

