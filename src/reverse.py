#!/usr/bin/env python3

import ipaddress
import socket
import re
from tools.color import *


def validate_ip(ipv4):
    try:
        ipaddress.ip_address(ipv4)
        return True
    except ValueError:
        return False
    
def validate_dns(dns_name):
    # Define the regex pattern for a valid DNS name
    pattern = re.compile(
        r"^(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE
    )

    # Split the DNS name by dots and validate each label
    if len(dns_name) > 255:
        return False
    
    labels = dns_name.split(".")
    for label in labels:
        if not pattern.match(label):
            return False

    # Optionally, check if DNS name resolves
    try:
        socket.gethostbyname(dns_name)
        return True
    except socket.error:
        return False
    
def validate_ip_dns(ip):
    
    if validate_ip(ip):
        return True
    elif validate_dns(ip):
        return False
    else:
        print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_RED} Invalid IP Address!!!")
    
def reverseIP(ip):

    if validate_ip(ip):
        try:
            ipv4 = socket.gethostbyaddr(ip)
            print(f"{BRIGHT_MAGENTA} [+]{BRIGHT_CYAN} Original Domain is : {ipv4[0]}")
        except Exception:
            print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_RED} Invalid IP Address!!!")
    elif validate_dns(ip):
        try:
            dns = socket.gethostbyname(ip)
            print(f"{BRIGHT_MAGENTA} [+]{BRIGHT_CYAN} Original IP Address : {dns}")
        except Exception:
            print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_RED} Invalid Domain Name!!!")

if __name__ == "__main__":
    reverseIP()