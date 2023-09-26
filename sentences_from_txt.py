file_name = input("Enter the file name: ")
query = input("Enter the query: ")

with open(file_name, "r") as file:
    sentence = file.read().lower().strip()

query = query.lower().strip()

num_occurrences = sentence.count(query)
print("Number of occurrences:", num_occurrences)
