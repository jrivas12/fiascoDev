def display_periodic_table(periodic_table):
    print("Periodic Table")
    print("{:<4} {:<6} {:<8} {:<8} {:<12} {:<8} {:<12} {:<12} {:<14} {:<14} {:<12} {:<8}".format(
        "Number", "Period", "Group", "Symbol", "Name", "Mass", "Radius", "Valence el.", "Stable isotopes",
        "Melting point", "Boiling point", "Density"
    ))
    print("-" * 144)

    for element in periodic_table:
        number = element['Number']
        period = element['Period']
        group = element['Group']
        symbol = element['Symbol']
        name = element['Name']
        mass = element['Mass']
        radius = element['Radius']
        valence_el = element['Valence el.']
        stable_isotopes = element['Stable isotopes']
        melting_point = element['Melting point']
        boiling_point = element['Boiling point']
        density = element['Density']

        print("{:<4} {:<6} {:<8} {:<8} {:<12} {:<8} {:<12} {:<12} {:<14} {:<14} {:<12} {:<8}".format(
            number, period, group, symbol, name, mass, radius, valence_el, stable_isotopes,
            melting_point, boiling_point, density
        ))

    print()

def parse_elements_data():
    periodic_table = []

    elements = [
        [55, 6, 1, "Cs", "Caesium", 132.9, 260, 1, 1, 302, 944, 1.9],
        [56, 6, 2, "Ba", "Barium", 137.33, 215, 2, 7, 1000, 1913, 3.65],
        [57, 6, 3, "La", "Lanthanum", 138.91, 195, 0, 1, 1193, 3730, 6.16],
        [58, 6, 3, "Ce", "Cerium", 140.12, 185, 0, 3, 1068, 3716, 6.77],
        [59, 6, 3, "Pr", "Praseodym", 140.91, 185, 0, 1, 1204, 3793, 6.48],
        # Add more elements here
    ]

    for element_data in elements:
        element = {
            'Number': element_data[0],
            'Period': element_data[1],
            'Group': element_data[2],
            'Symbol': element_data[3],
            'Name': element_data[4],
            'Mass': element_data[5],
            'Radius': element_data[6],
            'Valence el.': element_data[7],
            'Stable isotopes': element_data[8],
            'Melting point': element_data[9],
            'Boiling point': element_data[10],
            'Density': element_data[11]
        }
        periodic_table.append(element)

    return periodic_table

# Parse the elements data
periodic_table = parse_elements_data()

# Display the periodic table
display_periodic_table(periodic_table)