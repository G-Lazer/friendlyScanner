#!/bin/python
 
import sys
import socket
 
# syntax = python3 friendlyScanner [ipv4]
 
try:
    portStart = int(input("\nEnter the starting port: "))
    portEnd = int(input("Enter the ending port: "))
    print("\n")
 
except ValueError:
    print("\nYou must input ports by number.")
 
address = (sys.argv[1])
 
for port in range(portStart,portEnd):
    x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    response = x.connect_ex((address,port))
    if response == 0:
        print("Port {}: Open".format(port))
    x.close()
