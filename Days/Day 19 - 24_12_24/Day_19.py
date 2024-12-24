# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	23/12/2024

"""
Day 19: Dive Time and Profile  



"""

from colorama import Fore, Back, Style
import logging

scriptname: str = "Day_19.py"

# Logger Paramteres
filename: str = "C:/Users/simon/Git_Repos/100_project_in_100_days/Days/Day 19 - 24_12_24/log.log"
LOG_FORMAT = "|-- %(asctime)s --- %(levelname)s --- %(message)s --------|"

# Define logger
logging.basicConfig(filename = filename, 
	level = logging.DEBUG,
	format = LOG_FORMAT)
logger = logging.getLogger(__name__)

def start()-> None: # move to header file
	print(f'|---------------------------------------------------|')
	print(f'|================= PROGRAM STARTED =================|')
	print(f'|---------------------------------------------------|')
	print(f'\n')
	logger.info(f'***** {scriptname} Run *****')
def end()-> None:# move to header file
	print(f'\n')

	print(f'|---------------------------------------------------|')
	print(f'|================== PROGRAM ENDED ==================|')
	print(f'|---------------------------------------------------|')

def user_input()-> float:
	cylinder_size = input(f'What is your cylinder size? ')
	cylinder_size =  float(cylinder_size)
	logger.info(f'Cylinder Size: {cylinder_size}')

	cylinder_gas = input(f'How much gas is in your cylinder? (in bar) ')
	cylinder_gas =  float(cylinder_gas)
	logger.info(f'Cylinder Gas: {cylinder_gas}')

	predicted_depth = input(f'What is you predicted depth? ')
	predicted_depth = float(predicted_depth)
	logger.info(f'Planned Depth: {predicted_depth}')

	predicted_dive_time = input (f'What is you predicted dive time? ')
	predicted_dive_time = float(predicted_dive_time)
	logger.info(f'Planned Time: {predicted_dive_time}')


	consumption = input (f'What is your consumption? (avg consumption 25L/min) ')
	consumption = float(consumption)
	logger.info(f'Consumption: {consumption}')


	return cylinder_size,cylinder_gas,predicted_depth,predicted_dive_time,consumption

def gas_calculations(cylinder_gas,cylinder_size,predicted_depth,consumption)-> float:
	print(f'')
	reserve = cylinder_gas*0.333
	print(f'Reserve: {reserve}')
	logger.info(f'Reserve: {reserve}')

	useable_gas = cylinder_gas - reserve
	print(f'Useable Gas: {useable_gas}bar')
	logger.info(f'Useable (bar): {useable_gas}')


	useable_gas = useable_gas*cylinder_size
	print(f'Useable Gas: {useable_gas}L')
	logger.info(f'Useable (bar L): {useable_gas}')


	predicted_depth = (predicted_depth/10)+1
	logger.info(f'Depth (bar): {predicted_depth}')

	useable_gas = useable_gas/predicted_depth
	logger.info(f'Useable (L): {useable_gas}')

	dive_time = useable_gas/consumption
	logger.info(f'Dive Time (min): {dive_time}')

	print(f'Dive Time: {round(dive_time,2)} minutes')
	print(f'')

	return dive_time

def evaluation(predicted_dive_time,dive_time)-> None:

	if predicted_dive_time > dive_time:
		print(f'{colour("WARNING:", Fore.RED)} You do not have enought gas to compelte this dive.')
		logger.warning(f'WARNING ISSUED: {predicted_dive_time} > {dive_time}')
	elif predicted_dive_time <= dive_time:
		print(f'{colour("CLEAR:", Fore.GREEN)} Enjoy your dive!')
		logger.info(f'CLEAR: {predicted_dive_time} <= {dive_time}')
	else:
		print(f'{colour("ISSUE:", Fore.YELLOW)} Values Not Recognised!')
		logger.error(f'ISSUE: {predicted_dive_time} <= {dive_time}')

	#print(f'|    |Depth|Time|')
	#print(f'|Plan| {predicted_depth} |{predicted_dive_time}|')
	#print(f'| JD |||')
	#print(f'| JL |||')
	#print(f'| WC |||')
	
def colour(text: str, fg, bg=None) -> str:
	coloured_text = f'{fg}{text}{Style.RESET_ALL}'

	return coloured_text if bg is None else bg + coloured_text

def main():
	start()

	run = True

	while run == True:
		
		predicted_dive_time:float = 30.00
		predicted_depth:float = 20.00
		cylinder_size:float = 15.00
		cylinder_gas:float = 232.00
		reserve: float = 0.00
		useable_gas:float = 0.00
		consumption:float = 25.00

		cylinder_size,cylinder_gas,predicted_depth,predicted_dive_time,consumption = user_input()
		dive_time = gas_calculations(cylinder_gas,cylinder_size,predicted_depth,consumption)

		evaluation(predicted_dive_time,dive_time)

		print(f'')
		contiue = input(f'Do you want to run again? (y, n) ')
		print(f'')

		if contiue == 'n':
			break
		logger.info(f'## Loop restart ##')

	end()

if __name__ == '__main__':
	main()