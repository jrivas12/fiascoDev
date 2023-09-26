username = 'joe'
password = 'random'

correct = False

while not correct:
  username_input = input('Username:')
  password_input = input('Password:')
  if username_input == '-1' or password_input == '-1':
      break
  if username_input == username and password_input == password:
    print('User Authenticated: Welcome Back!')
    correct = True
  else:
    print('invalid password, pleae try again...\n')