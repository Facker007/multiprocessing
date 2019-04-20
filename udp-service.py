#!/usr/bin/python

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',6000))
while True:
	data,addr=s.recvfrom(1024)
	print "Connected by ",addr
	print "Recvied",data
	s.sendto(data,addr)
s.close()
