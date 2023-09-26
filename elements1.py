periodic_table = {
    'H': {'name': 'Hydrogen', 'atomic_number': 1, 'atomic_mass': 1.008, 'group': 'Nonmetal'},
    'He': {'name': 'Helium', 'atomic_number': 2, 'atomic_mass': 4.0026, 'group': 'Noble Gas'},
    'Li': {'name': 'Lithium', 'atomic_number': 3, 'atomic_mass': 6.94, 'group': 'Alkali Metal'},
    'Be': {'name': 'Beryllium', 'atomic_number': 4, 'atomic_mass': 9.0122, 'group': 'Alkaline Earth Metal'},
    # Add more elements here...
}

def display_periodic_table():
    print("Periodic Table")
    print("{:<4} {:<12} {:<14} {:<10}".format("Symbol", "Name", "Atomic Number", "Atomic Mass"))
    print("-" * 44)

    for symbol, element in periodic_table.items():
        name = element['name']
        atomic_number = element['atomic_number']
        atomic_mass = element['atomic_mass']
        print("{:<4} {:<12} {:<14} {:<10}".format(symbol, name, atomic_number, atomic_mass))

    print()

# Display the periodic table
display_periodic_table()

# Remove an element from the periodic table
symbol_to_remove = 'Be'
if symbol_to_remove in periodic_table:
    del periodic_table[symbol_to_remove]
    print(f"Removed {symbol_to_remove} from the periodic table.")
else:
    print(f"{symbol_to_remove} does not exist in the periodic table.")

# Display the updated periodic table
display_periodic_table()

