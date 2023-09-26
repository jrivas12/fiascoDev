def read_elements_data(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    elements = []
    headers = lines[0].split('\t')
    for line in lines[1:]:
        data = line.split('\t')
        element = dict(zip(headers, data))
        elements.append(element)
    
    return elements

def print_elements_table(elements):
    headers = elements[0].keys()
    print('|'.join(headers))
    print('-' * (len(headers) * 12))
    
    for element in elements:
        row = [element[header] for header in headers]
        print('|'.join(row))

file_name = 'elements_data.txt'
elements = read_elements_data(file_name)
print_elements_table(elements)
