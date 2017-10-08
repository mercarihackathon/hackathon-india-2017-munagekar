#Wire-P2P Wifi - Client Side
import socket
#username
user = 'nointernet'
#one time password
otp = 'defg'
#server local wlan address
sIp = '127.0.0.1'
#service port
servicePort = 22244


#create the socket
print 'Attempting to Contact Server'
serverSocket= socket.socket()                    
serverSocket.connect((sIp, servicePort))
print "Sending Credentials"
serverSocket.send(user)
print serverSocket.recv(50)
serverSocket.send(otp)
print serverSocket.recv(50)
serverSocket.send('Process Verification')
print 'Verification Pending'
authcode = serverSocket.recv(2)
if authcode =='F':
	print 'Print Access Failed'
else:
	print 'Access Granted Enjoy Wire-P2P Internet'
'''
print 'Credentials Sent'
print serverSocket.recv(1000)



print ('You will now be disconnected')
print ('Press enter when reconnected')
#input('Press enter when connected to')
'''


