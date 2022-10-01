
import socket

def scan_port(ip_addr, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((ip_addr, port))
	if result == 0:
		return True
	else:
		return False

res = scan_port("192.168.99.183", 5000)
print(res)