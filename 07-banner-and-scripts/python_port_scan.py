#!/usr/bin/python
import socket

# Prompt the user for an IP address to scan
ip_address = input("Enter IP address to scan: ")

# Define the range of ports to scan
start_port = 1
end_port = 65535

# Create a function to check  if a port is open or closed
def scan_port(ip_address, port):
	try:
		# Create a socket object
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		# Attempt to connect to the  given port
		result = sock.connect_ex((ip_address, port))
		if result == 0:
			#if the connection was successful, the port is open
			print(f"Port {port} is open")
		#close the socket connection
		sock.close()
	except:
		pass

# Loop through ports in the range and call the scan_port function
for port in range(start_port, end_port + 1):
	scan_port(ip_address, port)
