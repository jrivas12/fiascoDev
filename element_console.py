def read_elements_data(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    elements = []
    headers = lines[0].strip().split('\t')
    for line in lines[1:]:
        data = line.strip().split('\t')
        element = dict(zip(headers, data))
        elements.append(element)

    return elements


def print_elements_table(elements, column_widths):
    headers = elements[0].keys()

    # Print headers
    header_line = '|'.join(format(header, f' ^{width}') for header, width in zip(headers, column_widths))
    separator_line = '-' * (sum(column_widths) + len(column_widths) * 3 - 1)
    print(header_line)
    print(separator_line)

    # Print rows
    for element in elements:
        row = [format(element.get(header, ''), f' <{width}') for header, width in zip(headers, column_widths)]
        print('|'.join(row))


def view_elements_by_periodic_number(elements):
    while True:
        print("\n----- View Elements by Periodic Number -----")
        element_number = input("Enter the atomic number of the element (1-118), or 'q' to exit: ")

        if element_number == 'q':
            break

        found_element = False
        for element in elements:
            if element['Number'] == element_number:
                column_widths = [max(len(header), len(element[header])) for header in element.keys()]
                print_elements_table([element], column_widths)
                found_element = True
                break

        if not found_element:
            print("Element not found. Please try again.")


def view_elements_by_group(elements):
    while True:
        print("\n----- View Elements by Group -----")
        print("1. Group 1")
        print("2. Group 2")
        print("3. Group 3")
        print("4. Group 4")
        print("5. Group 5")
        print("6. Group 6")
        print("7. Group 7")
        print("8. Back to previous menu")

        group_choice = input("Enter your choice (1-8): ")

        if group_choice == '8':
            break

        group_elements = [element for element in elements if element['Group'] == group_choice]

        if len(group_elements) > 0:
            column_widths = [max(len(header), len(element[header])) for header in group_elements[0].keys()]
            print_elements_table(group_elements, column_widths)
        else:
            print("No elements found in the selected group.")


def display_noble_gases(elements):
    noble_gases = [element for element in elements if element['Group'] == '18']
    column_widths = [max(len(header), len(element[header])) for header in noble_gases[0].keys()]
    print_elements_table(noble_gases, column_widths)


def display_rare_metals(elements):
    rare_metals = [element for element in elements if element['Group'] in ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12']]
    column_widths = [max(len(header), len(element[header])) for header in rare_metals[0].keys()]
    print_elements_table(rare_metals, column_widths)


def display_radioactive_decay(elements):
    radioactive_elements = [element for element in elements if element['Stable isotopes'] == '']
    column_widths = [max(len(header), len(element[header])) for header in radioactive_elements[0].keys()]
    print_elements_table(radioactive_elements, column_widths)


def read_element_groups(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    element_groups = {}
    current_group = None

    for line in lines:
        line = line.strip()

        if line.startswith("Group"):
            group_number = line.split(':')[0].strip().replace("Group", "")
            current_group = []
            element_groups[group_number] = current_group
        elif line:
            element_data = line.split('\t')
   #         current_group.append(element_data)

    return element_groups


def view_elements_by_group_menu(element_groups):
    while True:
        print("\n----- View Elements by Group -----")
        for group_number, group_elements in element_groups.items():
            group_name = group_elements[0][4]
            print(f"{group_number}. {group_name}")

        print(f"{len(element_groups) + 1}. Back to previous menu")

        group_choice = input("Enter your choice (1-8): ")

        if group_choice == str(len(element_groups) + 1):
            break

        if group_choice in element_groups:
            elements = element_groups[group_choice]
            headers = elements[0]
            group_elements = [dict(zip(headers, data)) for data in elements]
            column_widths = [max(len(header), max(len(element[header]) for element in group_elements)) for header in headers]
            print_elements_table(group_elements, column_widths)
        else:
            print("Invalid choice. Please try again.")

# Main menu function
def main_menu():
    elements_file_name = 'elements_data.txt'
    groups_file_name = 'element_groups.txt'

    elements = read_elements_data(elements_file_name)
    element_groups = read_element_groups(groups_file_name)

    while True:
        print()
        print("{:-^45}".format(" Element's Program "))
        print("1. View elements by periodic number")
        print("2. View elements by group")
        print("3. Display noble gases")
        print("4. Display rare metals")
        print("5. Display radioactive decay")
        print("6. Display all elements")
        print("7. Exit")
        print("---------------------------------------------")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            view_elements_by_periodic_number(elements)
        elif choice == '2':
            view_elements_by_group_menu(element_groups)
        elif choice == '3':
            display_noble_gases(elements)
        elif choice == '4':
            display_rare_metals(elements)
        elif choice == '5':
            display_radioactive_decay(elements)
        elif choice == '6':
            column_widths = [max(len(header), max(len(element.get(header, '')) for element in elements)) for header in elements[0].keys()]
            print_elements_table(elements, column_widths)
        elif choice == '7':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the main menu
main_menu()
