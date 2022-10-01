
from scapy.all import *

def syn_scan(ip_addr, port): # stealth (SYN) scan

	ip_packet = IP(dst=ip_addr)
	syn_packet = ip_packet/TCP(dport=port, flags="S", seq=100) # SYN packet
	res_packet = sr1(syn_packet, timeout=1, verbose=0)

	if res_packet.getlayer(TCP).flags == "SA": # expect a SYN-ACK packet if port is open
		return True
	else:
		return False

# may need to send a RST packet?