import socket
import sys
host = 'localhost'
port = 50000
size = 1024
#create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', port)
print >> sys.stderr, '\n\nconnecting to %s port %s' % server_address
#now connect to the web server on port 80
# = the normal http port
s.connect (server_address)
try:
	message = 'This is the message. It will be repeated.'
	print >>sys.stderr, '\n\nsending "%s" ' % message
	bytes = s.sendto(message, server_address)
	#redo print >>sys.stderr, 'Number of bytes sent %s' % bytes
	
	returned_message, server=s.recvfrom(bytes)
	#REDO print >>sys.stderr, ' i got as far as s.recvfrom(bytes)'
	print >>sys.stderr, '\n\n!!!!!!!!!!!!!!!!!!!!!!!\n\nMessage returned is \n\n *************************\n\n %s \n \n' % returned_message, server



#	amount_received = 0
#	amount_expected = len(message)
#	print >>sys.stderr, 'length of message is "%s" ' %amount_expected

#	while amount_received < amount_expected:
#		data=s.recv(amount_expected)
#		amount_received += len(data)
#		print >>sys.stderr, 'received "%s"' % data
finally:
	print >>sys.stderr, 'closing socket'
	s.close()


