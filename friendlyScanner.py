#!/usr/bin/env python3

import socket

def scan_ports(address, start_port, end_port):
    print(f"\nScanning ports on {address} from {start_port} to {end_port}\n")

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((address, port))
            if result == 0:
                print(f"Port {port}: Open")

def get_address():
    while True:
        hostname = input("Enter the IPv4 address or hostname: ")
        try:
            address = socket.gethostbyname(hostname)
            print(f"Resolved hostname to {address}")
            return address
        except socket.gaierror:
            print(f"Could not resolve '{hostname}'. Please enter a valid IPv4 address:")
            continue

def main():
    address = get_address()

    while True:
        try:
            port_start = int(input("Enter the starting port: "))
            port_end = int(input("Enter the ending port: "))
            if port_start <= port_end:
                break
            else:
                print("The starting port must be less than or equal to the ending port.")
        except ValueError:
            print("\nError: You must input port numbers.")
            return

    scan_ports(address, port_start, port_end)

if __name__ == "__main__":
    main()

