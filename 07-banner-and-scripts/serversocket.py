#!/usr/bin/python

import socket

# set IP address
host = "10.0.0.200"

#create a socket object bind it to an IP address and port number
server_socket = socket.socket()
server_socket.bind((host, 6065))

#set the server to listen for  incoming connections
server_socket.listen(1)

#wait for a client connection
print("Waiting for a client to connect...")
client_socket, client_address = server_socket.accept()

#print client IP address and send a message
print("Got a connection from", client_address)
message = "Hello, scotejo!"
client_socket.send(message.encode())

#close the connection
client_socket.close()

