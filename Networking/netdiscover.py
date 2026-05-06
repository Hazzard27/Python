from scapy.all import ARP, Ether, srp

network = input("Enter network (e.g. 192.168.1.0/24): ")

# Create ARP request
arp = ARP(pdst=network)

# Broadcast MAC address
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether / arp

# Send packet and receive responses
result = srp(packet, timeout=2, verbose=0)[0]

print("IP Address\t\tMAC Address")
print("-" * 40)

for sent, received in result:
    print(f"{received.psrc}\t\t{received.hwsrc}")