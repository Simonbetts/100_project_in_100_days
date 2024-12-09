# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	09/12/2024

"""
Day 10: Object Banking app

print{f'dataterm   ->  1000 | 100%'}


"""

from Day_10 import BankAccount

def main() -> None:
	
	account_1 = BankAccount(1000)
	account_2 = BankAccount(100)

	# Withdraw and Deposit
	account_1.withdraw(50)
	account_2.deposit(100)
	print(f'Balance of account 1: £{account_1.balance}')
	print(f'Balance of account 2: £{account_2.balance}')
	print(f'')

	account_1.withdraw(40)
	account_2.deposit(100)

	account_1.withdraw(30)
	account_2.deposit(100)

	account_1.deposit(30)
	account_2.withdraw(20)

	# Transfer 


	# Transaction History
	print(f'Account 1 transaction history:\n{account_1.transaction_histroy}')
	print(f'')
	print(f'Account 2 transaction history:\n{account_2.transaction_histroy}')

if __name__ == '__main__':
	main()