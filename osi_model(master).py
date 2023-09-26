layers = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
	
	# Layer 7: Application
layers[6].extend(['Web Application Firewall', 'Load Balancer', 'API Gateway'])
	
	# Layer 6: Presentation
layers[5].extend(['Data Encryption', 'Data Compression'])
	
	# Layer 5: Session
layers[4].extend(['Session Management', 'Connection Tracking'])
	
	# Layer 4: Transport
layers[3].extend(['TCP Segmentation', 'UDP Checksum'])
	
	# Layer 3: Network
layers[2].extend(['Routing', 'IP Addressing'])
	
	# Layer 2: Data Link
layers[1].extend(['MAC Addressing', 'Switching', 'VLAN'])
	
	# Layer 1: Physical
layers[0].extend(['Ethernet', 'Fiber Optics'])
	
	# Sort devices within each layer
for layer in layers:
    layer.sort()
	
	# Determine the maximum number of devices in a layer
max_devices = max(len(layer) for layer in layers)
	
	# Display the layers and their devices in tabular format
print("OSI Model Layers and Devices:")
print("--------------------------------------------")
print("| {:^15} | {:^15} ".format("Layer", "Devices"))
print("|-----------------|-------------------------")
	
for i, layer in enumerate(layers, start=1):
    devices = layer + [''] * (max_devices - len(layer))
    print("| {:<15} | {:<15} ".format(f"Layer {i}", devices[0]))
	
    for device in devices[1:]:
        print("| {:<15} | {:<15} ".format("", device))
	
    print("|-----------------|-------------------------")