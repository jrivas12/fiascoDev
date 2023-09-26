osi_model = [
    ["Layer 7: Application"],
    ["Layer 6: Presentation"],
    ["Layer 5: Session"],
    ["Layer 4: Transport"],
    ["Layer 3: Network"],
    ["Layer 2: Data Link"],
    ["Layer 1: Physical"]
]
	
print("OSI Model Layers:")
print("------------------------------")
print("| {:^26} |".format("Layer"))
print("------------------------------")
	
for layer in osi_model:
    print("| {:<26} |".format(layer[0]))
	
print("------------------------------")