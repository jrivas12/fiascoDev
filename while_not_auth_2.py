username = 'joe'
password = 'random'

correct = False

while not correct:
    username_input = input('Username: ')
    if username_input == '-1':
        break
    password_input = input('Password: ')

    if username_input == username and password_input == password:
        print('User Authenticated: Welcome Back!')
        correct = True
    else:
        print('Invalid password, please try again...\n')

# print('Bye!')
