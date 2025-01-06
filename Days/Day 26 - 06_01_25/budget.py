import matplotlib.pyplot as plt
import numpy as np

class income(object):
	"""docstring for income"""
	def __init__(self, amount):
		super(income, self).__init__()
		self.amount = amount + amount

class outgoing(object):
	"""docstring for outgoing"""
	def __init__(self, arg):
		super(outgoing, self).__init__()
		self.arg = arg
		


def instantiate_income():
	#name:str = input("What is the name of the income?")
	name:str = "Work"
	amount: float = input(f"How much is {name}?")
	name = income(amount)

def instantiate_outgoing():
	#name:str = input("What is the name of the expanse?")
	name:str = "Rent"
	amount: float = input(f"How much is {name}?")

def main() -> None:
	work = income(10.00)
	print(work)


	income_1: float = 21.00
	outgoing_1: float = 14.00
	net: float = [income_1 - outgoing_1]

	total_pie = np.array([income_1,outgoing_1])

	#print(total_pie)
	#print(net)
	plt.figure(1)
	plt.pie(net, labels = ["Net Income"],autopct='%.2f%%')
	plt.show() 

	plt.figure(2)
	labels = ["Income","Outgoing"]
	plt.pie(total_pie, labels=labels,autopct='%.2f%%',startangle=90)
	plt.axis("equal")
	plt.legend(loc='lower left')
	plt.title('Total In/Out')
	plt.show() 






plt.show()


if __name__ == '__main__':
	main()