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

def print_elements_table(elements):
    headers = elements[0].keys()
    column_widths = [max(len(header), max(len(element.get(header, '')) for element in elements)) for header in headers]

    print('|'.join(format(header, f'^{width}') for header, width in zip(headers, column_widths)))
    print('-' * (sum(column_widths) + len(column_widths) * 3 - 1))

    for element in elements:
        row = [format(element[header], f'^{width}') for header, width in zip(headers, column_widths)]
        print('|'.join(row))

file_name = 'elements_data.txt'
elements = read_elements_data(file_name)
print_elements_table(elements)