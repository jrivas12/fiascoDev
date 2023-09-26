release_year = 1991

try:
	answer = int(input('When was Python first released?\t'))
	print(answer)
except ValueError:
	print('Fatal error. Please enter a valid year.')
else:
	if answer == release_year:
		print('Congratulations! That is correct.')
	elif 2023 >= answer > release_year:
		print('No, that is too late.')
	elif 1900 <= answer < release_year:
		print('No, that is too early.')
	else:
		print('Fatal error. Please try again!')
	
print('Program Terminated Successfully.')