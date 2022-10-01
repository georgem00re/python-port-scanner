
from modules.syn_scan import *

dest_ip_addr = "192.168.0.12"
dest_port = 5000

isOpen = syn_scan(dest_ip_addr, dest_port)