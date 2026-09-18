#!/usr/bin/env python

import socket

def ip_chg(ip):
    try:
        return socket.gethostbyname(ip)
    except socket.gaierror:
        return ip

if __name__ == "__main__":
        ip_chg()
