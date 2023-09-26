release_year = '1991'
answer = input('When was Python first released?''\t')
if answer == release_year:
	print('Congratulations! That is correct.')
elif answer > release_year:
	print('No, that is too late.')
elif answer < release_year:
	print('No, that is too early.')
elif answer != int(answer): 
	print('Fatal error. Please try again!')
print('Program Terminated Succesfully.')