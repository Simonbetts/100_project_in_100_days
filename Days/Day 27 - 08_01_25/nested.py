

condition_1 = True # Saftey Flag
condition_2 = True # Walk
condition_3 = True # Race
condition_4 = True # Control
condition_5 = True # Command

if condition_1 == True:
	print(f'Pass: Saftey Flag')
	#log
	if condition_2 == True:
		print(f'Pass: Walk')
		#log
		if condition_3 == True:
			print(f'Pass: Race')
			#log
			if condition_4 == True:
				print(f'Pass: Control')
				#log
				if condition_5 == True:
					print(f'Pass: Command')
					#log
				else:
					print(f'Failed: Command')
			else:
				print(f'Failed: Control')
		else:
				print(f'Failed: Race')
	else:
		print(f'Failed: Walk')
else:
	print(f'Failed: Saftey Flag')

print(f'\n ~~ Second Method: ~~ \n')

if condition_1 != False:
	print(f'Pass: Saftey Flag')
	#log
else:
	print(f'Failed: Saftey Flag')


if condition_2 != False:
	print(f'Pass: Walk')
	#log
else:
	print(f'Failed: Walk')

if condition_3 != False:
	print(f'Pass: Race')
	#log
else:	
	print(f'Failed: Race')

if condition_4 != False:
	print(f'Pass: Control')
	#log
else:
	print(f'Failed: Control')

if condition_5 != False:
	print(f'Pass: Command')
	#log
else:
	print(f'Failed: Command')





