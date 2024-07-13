#!/usr/bin/env python

import socket

def ip_chg(ip):

            try:
                    ipv4 = socket.gethostbyname(ip)
                    return ipv4
            except:
                    pass

if __name__ == "__main__":
        ip_chg()
