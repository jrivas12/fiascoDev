def extract_ansi(data):
    return data.decode('ascii', 'replace')

def convert_to_octal_decimal(data):
    return " ".join(f"{byte:03o}" for byte in data)

def convert_to_hexadecimal(data):
    return " ".join(f"{byte:02X}" for byte in data)

try:
    with open("data.bin", "rb") as file:
        binary_data = file.read()
        binary_data_lines = binary_data.splitlines()
except FileNotFoundError:
    print("\033[91mCould not open data.bin. Please create the file with some content.\033[0m")
else:
    print("\033[1m\033[95m" + r"""
 _______  _______  _______  _______           _______ 
(  __   )(  __   )(  __   )(  __   )|\     /|(  __   )
| (  )  || (  )  || (  )  || (  )  |( \   / )| (  )  |
| | /   || | /   || | /   || | /   | \ (_) / | | /   |
| (/ /) || (/ /) || (/ /) || (/ /) |  \   /  | (/ /) |
|   / | ||   / | ||   / | ||   / | |   ) (   |   / | |
|  (__) ||  (__) ||  (__) ||  (__) |   | |   |  (__) |
(_______)(_______)(_______)(_______)   \_/   (_______)
                                                     
    """ + "\033[0m")

    while True:
        print("\033[1m" + "Choose what to do with the data in 'data.bin':\033[0m")
        print("\033[94m1. Extract to ANSI format\033[0m")
        print("\033[93m2. Convert to hexadecimal format\033[0m")
        print("\033[92m3. Convert to octal decimal format\033[0m")
        print("\033[91mq. Quit\033[0m")

        user_choice = input("\033[95mEnter the number of your choice (or 'q' to quit):\033[0m ")

        if user_choice.lower() == "q":
            print("Exiting...")
            break
        elif user_choice == "1":
            print("\033[94mANSI Format:\033[0m")
            print(extract_ansi(binary_data))
        elif user_choice == "2":
            print("\033[93mHexadecimal Format:\033[0m")
            print(convert_to_hexadecimal(binary_data))
        elif user_choice == "3":
            print("\033[92mOctal Decimal Format:\033[0m")
            print(convert_to_octal_decimal(binary_data))
            print("\n\033[95mPress Enter to continue (or 'q' to go back to the main menu):\033[0m ", end="")
            user_input = input()
            if user_input.lower() == "q":
                print("Returning to the main menu...")
        else:
            print("\033[91mInvalid choice. Please enter a valid number.\033[0m")

    print("\033[1m\033[95mThank you for using the script! Goodbye!\033[0m")
