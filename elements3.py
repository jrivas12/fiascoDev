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
        [55, 6, 1, "Cs", "Caesium", 132.9, 260, 1, 1, 302, 944, 1.9],
        [60, 6, 3, "Nd", "Neodym", 144.24, 185, 0, 5, 1297, 3373, 7.00],
        [61, 6, 3, "Pm", "Promethium", 145.00, 185, 0, 0, 1315, 3273, 7.22],
        [62, 6, 3, "Sm", "Samarium", 150.36, 185, 0, 4, 1345, 2076, 7.54],
        [63, 6, 3, "Eu", "Europium", 151.96, 185, 0, 2, 1099, 1800, 6.16],
        [64, 6, 3, "Gd", "Gadolinium", 157.25, 180, 0, 6, 1585, 3523, 7.89],
        [65, 6, 3, "Tb", "Terbium", 158.92, 175, 0, 1, 1629, 3503, 8.25],
        [66, 6, 3, "Dy", "Dysprosium", 162.5, 175, 0, 7, 1680, 2840, 8.56],
        [67, 6, 3, "Ho", "Holmium", 163.93, 175, 0, 1, 1747, 2963, 8.78],
        [68, 6, 3, "Er", "Erbium", 167.26, 175, 0, 6, 1795, 2783, 9.05],
        [69, 6, 3, "Tm", "Thulium", 168.93, 175, 0, 1, 1818, 2220, 9.32],
        [70, 6, 3, "Yb", "Ytterbium", 173.04, 175, 0, 7, 1097, 1467, 6.97],
        [71, 6, 3, "Lu", "Lutetium", 174.97, 175, 0, 1, 1936, 3668, 9.84],
        [72, 6, 4, "Hf", "Hafnium", 178.49, 155, 0, 5, 2506, 4876, 13.31],
        [73, 6, 5, "Ta", "Tantalum", 180.95, 145, 0, 1, 3290, 5731, 16.68],
        [74, 6, 6, "W", "Tungsten", 183.84, 135, 0, 4, 3695, 5828, 19.26],
        [75, 6, 7, "Re", "Rhenium", 186.21, 135, 0, 1, 3459, 5869, 21.03],
        [76, 6, 8, "Os", "Osmium", 190.23, 130, 0, 6, 3306, 5285, 22.61],
        [77, 6, 9, "Ir", "Iridium", 192.22, 135, 0, 2, 2739, 4701, 22.65],
        [78, 6, 10, "Pt", "Platinum", 195.08, 135, 0, 4, 2045, 4100, 21.45],
        [79, 6, 11, "Au", "Gold", 196.97, 135, 0, 1, 1337, 3129, 19.32],
        [80, 6, 12, "Hg", "Mercury", 200.59, 150, 0, 7, 234, 630, 13.55],
        [81, 6, 13, "Tl", "Thallium", 204.38, 190, 3, 2, 577, 1746, 11.85],
        [82, 6, 14, "Pb", "Lead", 207.2, 180, 4, 3, 601, 2023, 11.34],
        [83, 6, 15, "Bi", "Bismuth", 208.98, 160, 5, 0, 544, 1837, 9.80],
        [84, 6, 16, "Po", "Polonium", 209.00, 190, 60, 0, 527, 1235, 9.20],
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

