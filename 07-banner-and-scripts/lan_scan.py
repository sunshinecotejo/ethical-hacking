#!/usr/bin/python3
import nmap

# define the LAN segment to scan
subnet = '10.0.0.200'
# create a new nmap scanner object
nm = nmap.PortScanner()

# scan the LAN segment using the nmap ping scan
nm.scan(hosts=subnet, arguments='-n -sP')
# get the list of hosts that responded to the ping scan
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts() if nm[x]['status']['state'] == 'up']

# print the list of hosts
print("List of hosts:")
for host, status in hosts_list:
	print(f"{host} ({status})")
# perform a service version scan on each host that responded to the ping scan
print("Service version scan:")
for host, status in hosts_list:
	print(f"Scanning {host}...")
	nm.scan(hosts=host, arguments='-sV')
	for port in nm[host]['tcp']:
		print(f"Port {port} is open: {nm[host]['tcp'][port]['product']} {nm[host]['tcp'][port]['version']}")
