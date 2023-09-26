import datetime
	
physical_layer = []
data_link_layer = ['Network Router', 'Network Switch', 'Network Firewall', 'Network Server']
	
physical_layer.extend(data_link_layer)
	
data_link_layer.insert(2, 'Network Gateway')
	
data_link_layer.pop(1)
data_link_layer.insert(1, 'Network Hub')
data_link_layer.sort(key=None, reverse=False)
physical_layer.sort(key=None, reverse=True)
	
now = datetime.datetime.now()
current_date = now.strftime("%m-%d-%Y")
	
print("Physical Layer               |  Data Link Layer")
print("------------------------------------------------")
for packet, device in zip(physical_layer, data_link_layer):
	print("{:<30} | {}".format(packet, device))
	
data_link_layer.insert(3, 'Network PC')
data_link_layer[0] = 'Network Media Converter'
data_link_layer[1] = 'Network Powerline Adapter'
data_link_layer[2] = 'Network VoIP Gateway'
	
print("\nUpdated Data Packets:")
print("-----------------------------------------------")
for i, packet in enumerate(data_link_layer, start=1):
	print("{:<4} | {}".format(i, packet))
	
print("-----------------------------------------------")
print("Updated Data Packets -", current_date)