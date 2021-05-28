#!/bin/python

import sys
import socket

# syntax = python3 friendlyScanner.py [ipv4]

try:
    port_start = int(input("\nEnter the starting port: "))
    port_end = int(input("Enter the ending port: "))
    print("\n")

except ValueError:
    print("\nYou must input ports by number.")

address = socket.gethostbyname(sys.argv[1])

try:

    for port in range(port_start, port_end):
        x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        response = x.connect_ex((address, port))
        if response == 0:
            print("Port {}: Open".format(port))
        x.close()

except socket.gaierror:
    print("Couldn't resolve hostname.\n")
