import socket
import sys

# create a socket object
client_socket = socket.socket()

# get server ip address
server = sys.argv[1]

# connect to the server
client_socket.connect((server, 6065))

# receive data from the server
serverdata = client_socket.recv(1024)

# print data
print(serverdata.decode())

# close the connection
client_socket.close() 
