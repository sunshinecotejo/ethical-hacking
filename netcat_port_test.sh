#!/bin/bash

# Prompt the user for a hostname or IP address to scan
echo -n "Enter hostname or IP address to scan: "
read target

# Loop through ports 1 to 1024
for port in {1..1024}
do
  # Use netcat to check if the port is open
  nc -z -w 1 $target $port 2> /dev/null
  if [ $? -eq 0 ] ; then
   echo "Port $port is open"
  fi
done
