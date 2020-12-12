# Python TCP Client B
import socket 

host = 'localhost'
port = 6666 
BUFFER_SIZE = 2000 
MESSAGE = raw_input("tcpClientB: Enter message/ Enter exit:")
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((host, port))

while MESSAGE != 'exit':
    tcpClientB.send(MESSAGE)     
    data = tcpClientB.recv(BUFFER_SIZE)
    print " Client received data:", data
    MESSAGE = raw_input("tcpClientB: Enter message to continue/ Enter exit:")

tcpClientB.close() 
