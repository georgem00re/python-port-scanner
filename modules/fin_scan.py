
from scapy.all import *

def fin_scan(ip_addr, port):

	ip_packet = IP(dst=ip_addr)
	fin_packet = ip_packet/TCP(dport=port, seq=100, flags="F") # FIN packet
	res_packet = sr1(fin_packet, timeout=1, verbose=0)

	if res_packet is None: # if port is open expect no response
		return True
	elif res_packet.getlayer(TCP).flags == "RA": # if port is closed expect RST-ACK packet
		return False