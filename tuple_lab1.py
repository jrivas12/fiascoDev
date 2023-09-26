wild = ["Tiger", "Zebra", "Panther", "Antelope"]
print (wild)
wild.append("Cat")
print (wild)
creatures = []
creatures.extend(wild)
print (creatures)
creatures.insert(2, "Dog")
print (creatures)
creatures.pop(1)
creatures.insert(1, "Giraffe")
print (creatures)
creatures.sort(key=None, reverse=False)
print (creatures)