#!/usr/bin/env python3

import argparse
from libs import *


def connection(uIP):
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
            print(f"\n{BRIGHT_MAGENTA}[+]---------- IP Information ----------[+]{BRIGHT_GREEN}")
            ipinfo(ip=uIP)
            print(f"\n{BRIGHT_MAGENTA}[+]---------- IP WHOIS ----------[+]{BRIGHT_GREEN}\n")
            check_whois(ip=uIP)
            print(f"\n{BRIGHT_MAGENTA}[+]---------- Completed ----------[+]{BRIGHT_GREEN}\n")

    except Exception as conn_error:
        print(f"{RED}Conn_Error : {conn_error}, Path ={__file__}")
    except KeyboardInterrupt:
        pass

class Main:
    @classmethod
    def args_main(cls):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            description=config.description
        )
        
        parser.add_argument("-d", type=str, metavar="Dns or IPv4", help="Enter IPv4 or DNS name")
        parser.add_argument("-r", type=str, metavar="Real Address", help="Reverse Real IPv4 or Domain name")
        parser.add_argument("-s", type=str, metavar="Subdomains", help="Print all SubDomains")
        parser.add_argument("-p", type=str, metavar="Port's", help="Print all Open Ports")
        parser.add_argument("-w", type=str, metavar="WAF check", help="Web Application Firewall check")
        parser.add_argument("-i", type=str, metavar="IP INFO", help="Get IP Infomation")
        parser.add_argument("-v", "--version", action="version", version=config.version, help="IPScanMaster")

        args = parser.parse_args()

        try:
            if args.d:
                uIP = args.d
            elif args.s:
                s = args.s
                enumerate_subdomain(domain=s)
                return None, s
            elif args.p:
                p = args.p
                scan_ports(ip=p)
            elif args.w:
                w = args.w
                check_waf(ip=w)
            elif args.r:
                r = args.r
                reverseIP(ip=r)
            elif args.i:
                i = args.i
                ipinfo(ip=i)
            else:
                parser.print_help()
                exit(1)

            uIP = uIP.replace("https://", "").replace("http://", "").rstrip("/")
            return uIP, None
        
        except UnboundLocalError: pass
        except ValueError as e:
            print(f"{RED}Value Error: {e}. Path = {__file__}{RESET}")
            exit(1)
        except Exception as e:
            print(f"{RED}Unexpected Error: {e}. Path = {__file__}{RESET}")
            exit(1)


if __name__ == "__main__":
    try:
        uIP, _ = Main.args_main()
        if uIP:
            ip_history(ip=uIP)  # Store in history file
            validate_ip_dns(uIP)
            connection(uIP)
    except Exception as e:
        pass