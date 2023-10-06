class Polyhedron:
    def __init__(self, name, wythoff, symbol, c_num, w_num, u_num, k_num, vertices, edges, faces, faces_by_type):
        self.name = name
        self.wythoff = wythoff
        self.symbol = symbol
        self.c_num = c_num
        self.w_num = w_num
        self.u_num = u_num
        self.k_num = k_num
        self.vertices = vertices
        self.edges = edges
        self.faces = faces
        self.faces_by_type = faces_by_type

    def __repr__(self):
        return self.name


class PolyhedraDatabase:
    def __init__(self):
        self.polyhedra = []

    def add_polyhedron(self, polyhedron):
        self.polyhedra.append(polyhedron)

    def remove_polyhedron(self, polyhedron):
        self.polyhedra.remove(polyhedron)

    def get_polyhedron_by_name(self, name):
        for polyhedron in self.polyhedra:
            if polyhedron.name == name:
                return polyhedron
        return None

    def get_polyhedra_by_wythoff(self, wythoff):
        matching_polyhedra = []
        for polyhedron in self.polyhedra:
            if polyhedron.wythoff == wythoff:
                matching_polyhedra.append(polyhedron)
        return matching_polyhedra

    def get_polyhedra_by_symbol(self, symbol):
        matching_polyhedra = []
        for polyhedron in self.polyhedra:
            if polyhedron.symbol == symbol:
                matching_polyhedra.append(polyhedron)
        return matching_polyhedra

    def get_polyhedra_by_vertex_count(self, vertex_count):
        matching_polyhedra = []
        for polyhedron in self.polyhedra:
            if polyhedron.vertices == vertex_count:
                matching_polyhedra.append(polyhedron)
        return matching_polyhedra

    def get_polyhedra_by_edge_count(self, edge_count):
        matching_polyhedra = []
        for polyhedron in self.polyhedra:
            if polyhedron.edges == edge_count:
                matching_polyhedra.append(polyhedron)
        return matching_polyhedra

    def get_polyhedra_by_face_count(self, face_count):
        matching_polyhedra = []
        for polyhedron in self.polyhedra:
            if polyhedron.faces == face_count:
                matching_polyhedra.append(polyhedron)
        return matching_polyhedra

    def get_polyhedra_by_face_type_count(self, face_type_count):
        matching_polyhedra = []
        for polyhedron in self.polyhedra:
            if polyhedron.faces_by_type == face_type_count:
                matching_polyhedra.append(polyhedron)
        return matching_polyhedra


# Example usage:
database = PolyhedraDatabase()

# Add polyhedra to the database
polyhedron1 = Polyhedron("Tetrahedron", "3 | 2 3", "Td", "C15", "W001", "U01", "K06", 4, 6, 4, "4{3}")
polyhedron2 = Polyhedron("Cube", "3 | 2 4", "Oh", "C18", "W003", "U06", "K11", 8, 12, 6, "6{4}")
polyhedron3 = Polyhedron("Octahedron", "4 | 2 3", "Oh", "C17", "W002", "U05", "K10", 6, 12, 8, "8{3}")

database.add_polyhedron(polyhedron1)
database.add_polyhedron(polyhedron2)
database.add_polyhedron(polyhedron3)

# Find polyhedra by name
found_polyhedron = database.get_polyhedron_by_name("Cube")
print(found_polyhedron)

# Find polyhedra by Wythoff symbol
matching_polyhedra = database.get_polyhedra_by_wythoff("3 | 2 3")
print(matching_polyhedra)

# Find polyhedra by number of vertices
matching_polyhedra = database.get_polyhedra_by_vertex_count(6)
print(matching_polyhedra)

# Remove a polyhedron from the database
database.remove_polyhedron(polyhedron2)

def create_polyhedra_database_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    database = []

    for line in lines:
        line = line.strip()
        if line:
            fields = line.split(',')

            name = fields[0].strip()
            wythoff = fields[1].strip().split('|')[0]
            symbol = fields[2].strip()
            c_num = fields[3].strip()
            w_num = fields[4].strip()
            u_num = fields[5].strip()
            k_num = fields[6].strip()
            vertices = int(fields[7].strip())
            edges = int(fields[8].strip())
            faces = int(fields[9].strip())
            faces_by_type = fields[10].strip()

            polyhedron = {
                'Name': name,
                'Wythoff': wythoff,
                'Sym.': symbol,
                'C#': c_num,
                'W#': w_num,
                'U#': u_num,
                'K#': k_num,
                'Vert.': vertices,
                'Edges': edges,
                'Faces': faces,
                'Faces by Type': faces_by_type
            }

            database.append(polyhedron)

    return database



# Example usage:
database = create_polyhedra_database_from_file('polyhedra.txt')