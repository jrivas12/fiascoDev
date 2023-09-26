try:
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    answer = str(name) + ", " + str(age)
    print('Hi', name, 'how are you doing today?')
    response = input("Enter 'y' for good or 'n' for bad: ")

    if response == 'y':
        print("That's good to know!")
    elif response == 'n':
        print("I hope you feel better.")
    else:
        print("Invalid response!")

except ValueError:
    print('Fatal error!')