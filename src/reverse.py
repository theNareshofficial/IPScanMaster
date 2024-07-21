#!/usr/bin/env python3

import socket
import ipaddress
import re

def is_valid_ip_or_dns(ip_or_dns):
    # Regular expression for validating DNS names
    dns_regex = re.compile(
        r'^(?=.{1,253}$)(?!-)(?!.*--)(?!.*\.$)([A-Za-z0-9-]{1,63}\.?)+[A-Za-z]{2,}$',
        re.IGNORECASE
    )

    # Function to check if the string is a valid DNS name
    def is_valid_dns(dns_name):
        if len(dns_name) > 253:
            return False
        if dns_name[-1] == '.':
            dns_name = dns_name[:-1]
        return all(dns_regex.match(label) for label in dns_name.split('.'))

    # Check if the input is a valid IP address
    try:
        ipaddress.ip_address(ip_or_dns)
        return True
    except ValueError:
        pass

    # Check if the input is a valid DNS name
    if is_valid_dns(ip_or_dns):
        return True

    print(f"{ip_or_dns} is not a valid IP address or DNS name!")
    return False

def reverseIP(ip):
        
        if is_valid_ip_or_dns(ip):
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