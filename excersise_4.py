release_year = '1991'

correct = False
while not correct:
	answer = input('When was Python first released?')
	
	if answer == release_year:
        print('Congratulations! That is correct.')
        correct = True
else:
    print('No, that\'s not it. Try again\n')
	
print('Bye!')