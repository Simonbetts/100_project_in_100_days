# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	01/12/2024

"""
Day 3: Virus Simulator 

create the mechnisum
work on a gui
"""

import Header
import time

def stats(infected,cured,dead,delt_t):
	print(f'')
	print(f'####')
	print(f'Infected: {int(infected)}')
	print(f'Cured: {int(cured)}')
	print(f'Dead: {int(dead)}')
	print(f'####')
	print(f'Time Elapsed = {delt_t}')


def main():

	Header.start()
	Header.description()
	
	# Simulation Parameters

	delt_t: int = 0
	infected: int = 10
	cured: int = 1
	dead:float = 0
	death_rate:float = 0.1;
	cure_delay:int = 2;


	stats(infected,cured,dead,delt_t)

	while True: # Overarching Simulation

		infected_rate:float = 1.1
		cursed_rate:float = 1.1

		
		# Simulaiton Mechnisums 
		if delt_t >= cure_delay:
			cured = cured+(cured*cursed_rate)


		infected = (infected+(infected*infected_rate))-cured
		dead = dead+(infected*death_rate)

		# Simulation Terminations 
		if infected < 1: 
			print(f'No Infected left') 
			break
		


		stats(infected,cured,dead,delt_t)

		delt_t = delt_t+1
		#time.sleep(1)
		
	Header.end()


if __name__ == '__main__':
	main()