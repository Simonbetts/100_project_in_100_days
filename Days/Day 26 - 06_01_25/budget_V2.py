import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
	
	work: float = 2100.00
	scholarship: float = 3000.00
	grant: float = 1000.00

	income_sum:float = 0
	# maybe more to a dictionary name:value
	income = [work, scholarship, grant]

	for x in income:
		income_sum:float = income_sum + x 

	rent: float = 900.00
	phone_bill: float = 20.00
	water_bill: float = 45.00
	electric_bill: float = 35.00
	amazon: float = 6.99
	fuel: float = 120.00
	food: float = 240.00
	house: float = 200.00

	outgoing_sum:float = 0
	# maybe more to a dictionary name:value
	outgoing = [rent,phone_bill,water_bill,electric_bill,amazon,fuel,food,house]

	for x in outgoing:
		outgoing_sum:float = outgoing_sum + x 

	net: float = income_sum - outgoing_sum

	print(f'|==================|')
	print(f'RESULTS')
	print(f'Total Incomes:   £{round(income_sum,2)}')
	print(f'Total Outogings: £{round(outgoing_sum,2)}')
	
	print(f'Total Net:       £{round(net,2)}')
	print(f'|==================|')

	total_pie = np.array([income_sum, outgoing_sum])
	#print(total_pie)

	#print(total_pie)
	'''
	print(net)
	plt.figure(1)
	plt.pie(net, labels = ["Net Income"],autopct='%1.1f%%')
	plt.axis("equal")
	plt.show() 
	'''

	plt.figure(2)
	labels = ["Income","Outgoing"]
	plt.pie(total_pie, labels=labels,autopct='%1.1f%%',startangle=90)
	plt.axis("equal")
	plt.legend(loc='lower left')
	plt.title('Total In/Out')
	plt.show() 






plt.show()


if __name__ == '__main__':
	main()