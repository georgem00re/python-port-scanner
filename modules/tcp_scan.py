
import socket

def tcp_scan(ip_addr, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((ip_addr, port))
	if result == 0:
		return True
	else:
		return False