def create_polyhedra_database_from_file(file_path):
    database = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    polyhedron_data = line.split(',')
                    name = polyhedron_data[0].strip()
                    wythoff = polyhedron_data[1].strip()
                    symbol = polyhedron_data[2].strip()
                    c_num = polyhedron_data[3].strip()
                    w_num = polyhedron_data[4].strip()
                    u_num = polyhedron_data[5].strip()
                    k_num = polyhedron_data[6].strip()
                    vertices = int(polyhedron_data[7].strip())
                    edges = int(polyhedron_data[8].strip())
                    faces = int(polyhedron_data[9].strip())
                    faces_by_type = polyhedron_data[10].strip()

                    polyhedron = {
                        'name': name,
                        'wythoff': wythoff,
                        'symbol': symbol,
                        'c_num': c_num,
                        'w_num': w_num,
                        'u_num': u_num,
                        'k_num': k_num,
                        'vertices': vertices,
                        'edges': edges,
                        'faces': faces,
                        'faces_by_type': faces_by_type
                    }
                    database.append(polyhedron)
                except IndexError:
                    print("Invalid data format in line: ", line)
    return database


def filter_polyhedra_by_field(database, field_name, field_value):
    filtered_polyhedra = []
    for polyhedron in database:
        if field_name in polyhedron and polyhedron[field_name] == field_value:
            filtered_polyhedra.append(polyhedron)
    return filtered_polyhedra


def group_polyhedra_by_attribute(database, attribute):
    grouped_polyhedra = {}
    for polyhedron in database:
        if attribute in polyhedron:
            attribute_value = polyhedron[attribute]
            if attribute_value in grouped_polyhedra:
                grouped_polyhedra[attribute_value].append(polyhedron)
            else:
                grouped_polyhedra[attribute_value] = [polyhedron]
    return grouped_polyhedra


def calculate_similarity(polyhedron1, polyhedron2):
    similarity_score = 0
    attributes_to_compare = ['vertices', 'edges', 'faces']
    for attribute in attributes_to_compare:
        if attribute in polyhedron1 and attribute in polyhedron2:
            value1 = polyhedron1[attribute]
            value2 = polyhedron2[attribute]
            similarity_score += abs(value1 - value2)
    return similarity_score


def find_most_similar_polyhedron(database, polyhedron):
    most_similar_polyhedron = None
    min_similarity_score = float('inf')
    for other_polyhedron in database:
        if other_polyhedron != polyhedron:
            similarity_score = calculate_similarity(polyhedron, other_polyhedron)
            if similarity_score < min_similarity_score:
                min_similarity_score = similarity_score
                most_similar_polyhedron = other_polyhedron
    return most_similar_polyhedron


def print_polyhedron(polyhedron):
    print('Name:', polyhedron['name'])
    print('Wythoff:', polyhedron['wythoff'])
    print('Symbol:', polyhedron['symbol'])
    print('C#:', polyhedron['c_num'])
    print('W#:', polyhedron['w_num'])
    print('U#:', polyhedron['u_num'])
    print('K#:', polyhedron['k_num'])
    print('Vertices:', polyhedron['vertices'])
    print('Edges:', polyhedron['edges'])
    print('Faces:', polyhedron['faces'])
    print('Faces by Type:', polyhedron['faces_by_type'])
    print()


def interactive_polyhedra_comparison():
    file_path = 'polyhedra.txt'
    database = create_polyhedra_database_from_file(file_path)

    while True:
        print("--- Polyhedra Comparison ---")
        print("1. Filter polyhedra by field")
        print("2. Group polyhedra by attribute")
        print("3. Find most similar polyhedron")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            field_name = input("Enter the field name to filter by: ")
            field_value = input("Enter the field value to filter by: ")
            filtered_polyhedra = filter_polyhedra_by_field(database, field_name, field_value)
            print("Filtered Polyhedra:")
            for polyhedron in filtered_polyhedra:
                print_polyhedron(polyhedron)

        elif choice == '2':
            attribute = input("Enter the attribute to group polyhedra by: ")
            grouped_polyhedra = group_polyhedra_by_attribute(database, attribute)
            print("Grouped Polyhedra:")
            for attribute_value, polyhedra in grouped_polyhedra.items():
                print(f"Attribute: {attribute_value}")
                for polyhedron in polyhedra:
                    print_polyhedron(polyhedron)
                print()

        elif choice == '3':
            polyhedron_name = input("Enter the name of the polyhedron: ")
            target_polyhedron = None
            for polyhedron in database:
                if polyhedron['name'].lower() == polyhedron_name.lower():
                    target_polyhedron = polyhedron
                    break
            if target_polyhedron:
                similar_polyhedron = find_most_similar_polyhedron(database, target_polyhedron)
                print("Most Similar Polyhedron:")
                print_polyhedron(similar_polyhedron)
            else:
                print("Polyhedron not found in the database.")

        elif choice == '4':
            break

        print()

interactive_polyhedra_comparison()