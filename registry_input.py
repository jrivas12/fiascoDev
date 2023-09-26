registry = [] 
	
while True:
    vector = input("Input an entry (or '-1' to exit): ")
	
    if vector == "-1":
        break  
	
registry.append(vector) 
	
print("List of registry:")
for vector in registry:
    print(vector)