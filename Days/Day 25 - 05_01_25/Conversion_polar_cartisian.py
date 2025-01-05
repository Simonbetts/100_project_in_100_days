


from math import *

x:float = 0
y:float = 0
r:float = 0
theta:float = 0

x = 1.0
y = 1.0


def start() -> None:
	print(f'|===================================================|')
	print(f'|================= PROGRAM STARTED =================|')
	print(f'|===================================================|')
	print(f'')

def end() -> None:
	print(f'')
	print(f'|===================================================|')
	print(f'|================== PROGRAM ENDED ==================|')
	print(f'|===================================================|')
	
def panel() -> None:

	conversion: str = input(f'What would you like to convert? Pol->Car (car) Car->Pol (pol)')

	if conversion == "car":
		print('car')
	elif conversion == "pol":
		print('pol')
	else:
		print('Error: Input not Regognised')

def cartisiantopolar() -> float:
	r = sqrt((x*x)+(y*y))
	print(f'r = {round(r,2)} m')
	theta = atan((y/x))
	theta_deg = theta*(180/3.1415)
	print(f'theta = {round(theta,2)} radians ({round(theta_deg,2)} degrees)')
	print(f'')

def polartocartisian() -> float:
	x = r*cos(theta)
	y = r*sin(theta)

	print(f'x = {round(x,2)} m')
	print(f'y = {round(y,2)} m')


def main():
	start()

	panel()
	print(f'Program did something here')

	end()

if __name__ == '__main__':
	main()