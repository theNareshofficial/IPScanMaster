#!/usr/bin/env python

from libs.imports import *

clrscr()
banner()


uIP = input(f"{GREEN}[+] Enter Your DNS or IPv4 : {CYAN}").replace("https://", "").replace("http://", "")
ip_history(ip=uIP)
is_ip_addr(uIP)

def connection():
        global uIP

        try:
                if inet_conn() == 0:

                        print(f"\n{YELLOW}[+]---------- Checking Your Original IP ----------[+]{RESET}{GREEN}\n")
                        reverseIP(ip=uIP)
                        print(f"\n{YELLOW}[+]---------- Checking Your IP Reachable ----------[+]{GREEN}\n")
                        ip_Reachable(ip=uIP)
                        print(f"\n{YELLOW}[+]---------- Checking WAF(Web Application Firewall) ----------[+]{GREEN}\n")
                        check_waf(ip=uIP)
                        uIP = ip_chg(ip=uIP)
                        print(f"\n{YELLOW}[+]---------- IP Information ----------[{GREEN}+]")
                        ipinfo(ip=uIP)
                        print(f"\n{YELLOW}[+]---------- Checking Open Port's ----------[+]{GREEN}\n")
                        scan_ports(ip=uIP)
                        print(f"\n{YELLOW}[+]---------- IP WHOIS ----------[+]{GREEN}\n")
                        check_whois(ip=uIP)
                        print(f"\n{YELLOW}[+]---------- Completed ----------[+]{GREEN}\n")
                else:
                        exit(None)
        
        except Exception as e:
                print(f"{RED}Error : {e}")

        except KeyboardInterrupt:
                pass

if __name__ == "__main__":
        connection()
