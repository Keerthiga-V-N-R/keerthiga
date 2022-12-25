#!/usr/bin/python
import socket
from termcolor import colored
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="192.168.43.107"

def portscanner(port):
	if sock.connect_ex((host,port)):
		print(colored("Port %d is closed"%(port),'red'))
	else:
		print(colored("Port %d is closed"%(port),'green'))
for port in range(1,1001):
	portscanner(port)

