#!/usr/bin/env python3

from libs import *

clrscr()
banner()

uIP = input(f"{BRIGHT_GREEN}[+] Enter Your DNS or IPv4 : {BRIGHT_CYAN}").replace("https://", "").replace("http://", "")

ip_history(ip=uIP)      # It's store in your history file
validate_ip_dns(uIP)

def connection():
        global uIP

        try:
                if inet_conn() == 0:

                        print(f"\n{BRIGHT_MAGENTA}[+]---------- Checking Your Original IP ----------[+]{RESET}{BRIGHT_GREEN}\n")
                        reverseIP(ip=uIP)
                        print(f"\n{BRIGHT_MAGENTA}[+]---------- Checking Your IP Reachable ----------[+]{BRIGHT_GREEN}\n")
                        ip_Reachable(ip=uIP)
                        print(f"\n{BRIGHT_MAGENTA}[+]---------- Checking WAF(Web Application Firewall) ----------[+]{BRIGHT_GREEN}\n")
                        check_waf(ip=uIP)
                        print(f"\n{BRIGHT_MAGENTA}[+]---------- Checking Sub-Domain's ----------[+]{BRIGHT_GREEN}\n")
                        enumerate_subdomain(domain=uIP)
                        print(f"\n{BRIGHT_MAGENTA}[+]---------- Checking Open Port's ----------[+]{BRIGHT_GREEN}\n")
                        scan_ports(ip=uIP)
                        uIP = ip_chg(ip=uIP)
                        print(f"\n{BRIGHT_MAGENTA}[+]---------- IP Information ----------[{BRIGHT_GREEN}+]")
                        ipinfo(ip=uIP)
                        print(f"\n{BRIGHT_MAGENTA}[+]---------- IP WHOIS ----------[+]{BRIGHT_GREEN}\n")
                        check_whois(ip=uIP)
                        print(f"\n{BRIGHT_MAGENTA}[+]---------- Completed ----------[+]{BRIGHT_GREEN}\n")
                else:
                        exit(None)
        
        except Exception as conn_error:
                print(f"{RED}Error : {conn_error}")
        except KeyboardInterrupt:
                pass

if __name__ == "__main__":
        connection()
