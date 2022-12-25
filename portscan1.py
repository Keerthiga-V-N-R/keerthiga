#!/usr/bin/python
#port scanning
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="192.168.43.107"
port=443
def portscanner(port):
	if sock.connect_ex((host,port)):
		print("Port %d is closed"%(port))
	else:
		print("Port %d is closed"%(port))
portscanner(port)
