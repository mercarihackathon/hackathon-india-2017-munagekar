#Wiber-P2P Wifi - Server Side
#Run as root
#Depends on Create wifi
import os
import subprocess
import socket

'''
#Constants
#Ethernet Interface
eInf ='enp3s0f1'
#Wifi Interface
wInf = 'wlp2s0'
wName = 'Wiber'

'''
fIp = '127.0.0.1'
suser= 'internetguy'
servicePort = 22244
authPort = 33355

#Begin launch
print 'Launching Server'

serverPort = socket.socket()
#bind the server to address where it will accept connections         
serverPort.bind(('127.0.0.1',servicePort))
print 'Server started'
serverPort.listen(2)
print 'Waiting for connection'

while True:

	c, addr = serverPort.accept()
	print 'Got connection from',addr
	user=c.recv(32)
	c.send('Server got user')
	otp=c.recv(10)
	c.send('Server got otp')
	print 'Got Credentials'
	
	
	print 'Begining verification'	
	veriSocket= socket.socket()                    
	veriSocket.connect((fIp, authPort))
	veriSocket.send(suser)
	print veriSocket.recv(100)
	veriSocket.send(user)
	print veriSocket.recv(100)
	veriSocket.send(otp)
	print veriSocket.recv(100)
	veriSocket.send('Process verification')
	authCode=veriSocket.recv(2)
	c.recv(100)
	if authCode =='F':
		print 'Auth Unsuccessful'
		print 'Access Denied to the Client'
		c.send('F')
	else:
		print 'Auth Successful'
		print 'Access Perimited'
		print 'Access To VPN allowed'
		c.send('T')
	'''
	if authCode=='F':
		c.send('F')
		print 'Auth failed rejected client'
		print 'Internet cannot be availed by the client'
		continue
	else:
		c.send('S')
		print 'Authentication succeeded'
		print 'Provide access'
	c.close()
	'''
	


