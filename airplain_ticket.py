seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
n = 0

while n < 10:
    my_seat = 0

    print("Choose the arrangement you want:")
    print("Enter 1 for First Class")
    print("Enter 2 for Economy Class")
    my_num = int(input())

    if my_num == 1:
        print("You chose First Class")
        if 0 in seats[:5]:
            for i in range(5):
                if seats[i] == 0:
                    my_seat = i + 1
                    seats[i] = 1
                    print("Your seat number is", my_seat)
                    break
        else:
            print("First Class seats are full.")
            print("Would you like to try Economy Class? (Y/N)")
            choice = input()
            if choice.upper() == "Y":
                for i in range(5, 10):
                    if seats[i] == 0:
                        my_seat = i + 1
                        seats[i] = 1
                        print("Your seat number is", my_seat)
                        break
            else:
                print("Next flight leaves in 3 hours.")

    elif my_num == 2:
        print("You chose Economy Class")
        if 0 in seats[5:10]:
            for i in range(5, 10):
                if seats[i] == 0:
                    my_seat = i + 1
                    seats[i] = 1
                    print("Your seat number is", my_seat)
                    break
        else:
            print("Economy Class seats are full.")
            print("Would you like to try First Class? (Y/N)")
            choice = input()
            if choice.upper() == "Y":
                for i in range(5):
                    if seats[i] == 0:
                        my_seat = i + 1
                        seats[i] = 1
                        print("Your seat number is", my_seat)
                        break
            else:
                print("Next flight leaves in 3 hours.")

    n += 1
