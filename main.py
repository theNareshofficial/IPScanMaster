#!/usr/bin/env python

from libs.imports import *

clrscr()

banner()

uIP = input("[+] Enter Your DNS or IPv4 : ")

is_ip_addr(uIP)

def connection():

        try:
                if inet_conn() == 0:

                        print("\n[+]---------- Checking Your Original IP ----------[+]\n")
                        reverseIP(ip=uIP)
                        print("\n[+]---------- Checking Your IP Reachable ----------[+]\n")
                        ip_Reachable(ip=uIP)
                        print("\n[+]---------- Checking WAF(Web Application Firewall) ----------[+]\n")
                        check_waf(ip=uIP)
                        print("\n[+]---------- IP Information ----------[+]")
                        ipinfo(ip=uIP)
                        print("\n[+]---------- Checking Open Port's ----------[+]\n")
                        scan_ports(ip=uIP)
                        print("\n[+]---------- IP WHOIS ----------[+]\n")
                        check_whois(ip=uIP)
                        print("\n[+]---------- Completed ----------[+]\n")
                else:
                        exit(None)
        
        except Exception as e:
                print(f"Error : {e}")

        except KeyboardInterrupt:
                pass

if __name__ == "__main__":
        connection()
