#Wiber-P2P Wifi - Facilitator Side
import socket
print 'Launching Facilitator'

#Will be inside an Sql Database
#will have username, otp, privatepassword, credits
facilitatorcash=0
database=[['internetguy','password','abcd',40],['nointernet','12345678','abcd',100]]

authPort = 33355
facilitatorPort = socket.socket()         
facilitatorPort.bind(('',authPort))
print 'Server started'
print 'Balance=',facilitatorcash
facilitatorPort.listen(2)
print 'Waiting for connection'

while True:

	s, addr = facilitatorPort.accept()
	print 'Got connection from',addr
	suser=s.recv(32)
	s.send('VServer Got server user')
	cuser=s.recv(32)
	s.send('VServer Got client user')
	otp=s.recv(4)
	s.send('Vserver Got Otp')
	s.recv(100)
	
	authcode=0
	for ue in database:
		if ue[0]==cuser and ue[2]==otp:
			ue[3]-=2
			authcode=1
			break
	if authcode ==1:
		s.send('S')
		for ue in database:
			if ue[0]==suser:
				ue[3]+=1
				facilitatorcash+=1
				break
	else:
		s.send('F')