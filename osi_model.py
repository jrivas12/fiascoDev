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
	
# Simulate removal of a device from Layer 4
layers[3].pop(1)
	
# Display the layers and their devices
for i, layer in enumerate(layers, start=1):
    print(f"Layer {i}:")
    for device in layer:
        print(f"- {device}")
    print()