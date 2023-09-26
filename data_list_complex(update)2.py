import datetime
	
cyber_network = []
data_packets = ['Network Router', 'Network Switch', 'Network Firewall', 'Network Server']
	
cyber_network.extend(data_packets)
	
data_packets.insert(2, 'Network Gateway')
	
data_packets.pop(1)
data_packets.insert(1, 'Network Hub')
data_packets.sort(key=None, reverse=False)
cyber_network.sort(key=None, reverse=True)
	
now = datetime.datetime.now()
current_date = now.strftime("%m-%d-%Y")
	
print("Network Hardware               |  Cyber Network")
print("------------------------------------------------")
for packet, device in zip(data_packets, cyber_network):
    print("{:<30} | {}".format(packet, device))

data_packets.insert(3, 'Network PC')
data_packets[-1] = 'Network Media Converter'
data_packets[-2] = 'Network Powerline Adapter'
data_packets[-3] = 'Network VoIP Gateway'
	
print("\nUpdated Data Packets:")
print("-----------------------------------------------")
for i, packet in enumerate(data_packets, start=1):
    print("{:<4} | {}".format(i, packet))

print("-----------------------------------------------")
print("Updated Data Packets -", current_date)