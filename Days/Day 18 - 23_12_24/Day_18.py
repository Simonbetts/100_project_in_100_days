# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	23/12/2024

"""
Day 18:  



"""

from colorama import Fore, Back, Style
import time
import logging
import random


scriptname: str = "Day_18.py"

# Logger Paramteres
filename: str = "C:/Users/simon/Git_Repos/100_project_in_100_days/Days/Day 18 - 23_12_24/log.log"
LOG_FORMAT = "| %(asctime)s === %(levelname)s === %(message)s ========|"

data_filename: str = "C:/Users/simon/Git_Repos/100_project_in_100_days/Days/Day 18 - 23_12_24/data.log"
DATA_LOG_FORMAT = "%(asctime)s , %(message)s"


# Define logger
logging.basicConfig(filename = filename, 
	level = logging.DEBUG,
	format = LOG_FORMAT)
logger = logging.getLogger(__name__)

data_logger = logging.getLogger(__name__)

# Define colour function
def colour(text: str, fg, bg=None) -> str:
	coloured_text = f'{fg}{text}{Style.RESET_ALL}'

	return coloured_text if bg is None else bg + coloured_text


def inspect_data(raw_data) -> None:
	data_therhold:int = 50

	if raw_data >= data_therhold:
		print(f'Status: {colour("Activite", Fore.GREEN)}')
		logger.info(f'System Setting: {raw_data} Status: Active')
	elif raw_data < data_therhold:
		print(f'Status: {colour("Inactive", Fore.RED)}')
		logger.info(f'System Setting: {raw_data} Status: Inactive"')
	else:
		print(f'! SENSOR VALUE NOT RECOGNISED !')
		logger.warning(f'! SENSOR VALUE NOT RECOGNISED !')

def real_time_data()->int:

	raw_data:int = int((random.random()*100))
	#data_logger.info(raw_data)
	return raw_data


def main()-> None:
	logger.info(f'***** {scriptname} Run *****')

	count:int = 0

	while count < 10:
		
		condition:int = int((random.random()*100))
		inspect_data(condition)
		count = count+1

	for x in range(100):
		data:int = real_time_data()
		print(f'Raw Data Value: {data}' )

	

if __name__ == '__main__':
	main()