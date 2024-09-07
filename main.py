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
            print(f"\n{BRIGHT_MAGENTA}[+]---------- Checking Sub-Domains ----------[+]{BRIGHT_GREEN}\n")
            enumerate_subdomain(domain=uIP)
            print(f"\n{BRIGHT_MAGENTA}[+]---------- Checking Open Ports ----------[+]{BRIGHT_GREEN}\n")
            scan_ports(ip=uIP)
            print(f"\n{BRIGHT_MAGENTA}[+]---------- Dirsearch ----------[+]{BRIGHT_GREEN}\n")
            DirSearch.search(self=DirSearch, ip=uIP)
            uIP = ip_chg(ip=uIP)
            print(f"\n{BRIGHT_MAGENTA}[+]---------- IP Information ----------[+]{BRIGHT_GREEN}")
            ipinfo(ip=uIP)
            print(f"\n{BRIGHT_MAGENTA}[+]---------- IP WHOIS ----------[+]{BRIGHT_GREEN}\n")
            check_whois(ip=uIP)
            print(f"\n{BRIGHT_MAGENTA}[+]---------- Completed ----------[+]{BRIGHT_GREEN}\n")

    except KeyboardInterrupt:
        print(f"{RED}Operation canceled by user.{RESET}")
        exit(0)
    except Exception as conn_error:
        print(f"{RED}Conn_Error : {conn_error}, Path ={__file__}{RESET}")

class Main:
    @classmethod
    def args_main(cls):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            description=config.description
        )
        
        parser.add_argument("-u", type=str, metavar="url", help="Enter IPv4 or DNS name")
        parser.add_argument("-m", type=str, metavar="Mode", required=True, choices=["attack", "scan"], help="Select the Mode for Attack or Scan")
        parser.add_argument("-r", type=str, metavar="Real Address", help="Reverse Real IPv4 or Domain name")
        parser.add_argument("-s", type=str, metavar="Subdomains", help="Print all SubDomains")
        parser.add_argument("-p", type=str, metavar="Ports", help="Print all Open Ports")
        parser.add_argument("-d", type=str, metavar="DirSearch", help="Small Directory Search")
        parser.add_argument("-w", type=str, metavar="WAF check", help="Web Application Firewall check")
        parser.add_argument("-i", type=str, metavar="IP INFO", help="Get IP Information")
        parser.add_argument("-v", "--version", action="version", version=config.version, help="IPScanMaster")

        args = parser.parse_args()

        try:
            uIP = None
            if args.m == "scan":
                if args.u:
                    uIP = args.u
                elif args.s:
                    enumerate_subdomain(domain=args.s)
                    return None, args.s
                elif args.p:
                    scan_ports(ip=args.p)
                    return None, args.p
                elif args.d:
                    DirSearch.search(self=DirSearch, ip=args.d)
                elif args.w:
                    check_waf(ip=args.w)
                    return None, args.w
                elif args.r:
                    reverseIP(ip=args.r)
                    return None, args.r
                elif args.i:
                    ipinfo(ip=args.i)
                    return None, args.i
                else:
                    parser.print_help()
                    exit(1)
            elif args.m == "attack":
                if args.d:
                    uIP = args.u
                    attacker = Attacking(IP=uIP) 
                    attacker.run_commands()
                    exit(0)
                else:
                    print("IP or DNS is required for attack mode.")
                    exit(1)
            else:
                parser.print_help()
                exit(1)

            if uIP:
                uIP = uIP.replace("https://", "").replace("http://", "").rstrip("/")
            return uIP, None
        
        except ValueError as e:
            print(f"{RED}Value Error: {e}. Path = {__file__}{RESET}")
            exit(1)
        except Exception as e:
            print(f"{RED}Unexpected Error: {e}. Path = {__file__}{RESET}")
            exit(1)


if __name__ == "__main__":
    TimeZone.start_time()
    uIP = None
    try:
        uIP, _ = Main.args_main()
        if uIP:
            validate_ip_dns(uIP)
            connection(uIP)
    except KeyboardInterrupt:
        print(f"{RED}Execution interrupted by user.{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
    finally:
        TimeZone.end_time()
        if uIP:
            ip_history(ip=uIP)  # Store in history file