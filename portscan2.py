#!/usr/bin/python
#port scanning by getting host and port as user input
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=input("Enter host:")
port=int(input("Enter port:"))
socket.setdefaulttimeout(2)
def portscanner(port):
	if sock.connect_ex((host,port)):
		print("Port %d is closed"%(port))
	else:
		print("Port %d is closed"%(port))
portscanner(port)

