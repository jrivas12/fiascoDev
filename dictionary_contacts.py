def access_contact_list(contacts):
   
    print("Printing all contact values:")
    for contact in contacts.values():
        print(contact)
    print()

    print("Retrieving a specific contact value:")
    name = contacts.get('name')
    print(f"Name: {name}")
    print()

    print("Printing all contact key-value pairs:")
    for key, value in contacts.items():
        print(f"{key}: {value}")
    print()

    print("Searching for a specific contact key:")
    key_to_find = 'email'
    found = False
    while not found:
        if key_to_find in contacts:
            print(f"Found contact key: {key_to_find}")
            found = True
        else:
            print(f"Contact key '{key_to_find}' not found")
            key_to_find = input("Enter another key to search: ")
    print()

    try:
        print(contacts['address'])
    except KeyError:
        print("Contact key 'address' does not exist")
        print()

contact_list = {
	'name': 'John Doe',
    'category': 'Backend Developer',
    'email': 'johndoe@developer.com',
    'phone': '555-555-5555',
    'location': 'Weslaco, Texax, United States'
}


access_contact_list(contact_list)