#!/usr/bin/env python

import socket

def is_ip_addr(input_string):
            try:
                    socket.inet_aton(input_string)
                    return True
            except socket.error:
                    return False

def reverseIP(ip):
        
        if is_ip_addr(ip):
                try:
                        ipv4 = socket.gethostbyaddr(ip)
                        print(f"Original Domain Name: {ipv4[0]}")
                except socket.herror:
                        print(f"{ip}: Invalid IP or no reverse DNS available!")
                        exit(1)
        else:
                try:
                        dns = socket.gethostbyname(ip)
                        print(f"Original IP Address : {dns}")
                except socket.gaierror:
                        print(f"{ip}: Invalid DNS or no reverse IPv4 available!")
                        exit(1)

if __name__ == "__main__":
        reverseIP()