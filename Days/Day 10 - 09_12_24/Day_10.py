# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	09/12/2024

"""
Day 10: Object Banking app

print{f'dataterm   ->  1000 | 100%'}


"""
from datetime import datetime
from enum import StrEnum, auto

class TransactionType(StrEnum):
	DEPOSIT = auto()
	WITHDEAWAL = auto()
	TRANSFER = auto()

Transaction = tuple[TransactionType, datetime, int]

class InsufficientBalanceError(Exception):
	pass

class BankAccount():
	"""docstring for account"""
	def __init__(self, initial_balance:float = 0) -> None:
		self.initial_balance = initial_balance
		self.balance = initial_balance
		self.transaction_histroy: list[Transaction] = []

		#self.tansaction_histroy

	def deposit(self, amount:float = 0) -> None:
		self.balance += amount
		self.transaction_histroy.append(
			(TransactionType.DEPOSIT,datetime.now(),amount)
			)
		# self. add to transaction history

	def withdraw(self, amount:float = 0) -> None:
		self.balance -= amount
		self.transaction_histroy.append(
			(TransactionType.WITHDEAWAL,datetime.now(),amount)
			)
		# self. add to transacation histroy
		'''
		def transfer(self, other: BankAccount, amount:float = 0) -> None:
		if not self.sufficent_balance(amount):
			raise InsufficentBalanceError
		timestamp = datetime.now()
		self._balance -= amount
		other._balance += amount
		# self. add to transacation histroy
		'''

		def sufficent_balance(self,amount: float) -> bool:
			return self.balance

'''
		@property
		def balance(self):
			return self._balance
'''

		
class insufficiant_funds(Exception):
	pass

Account_1 = BankAccount()

		

