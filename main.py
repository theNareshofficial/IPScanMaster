#!/usr/bin/env python3

import argparse
from libs import *

def connection(uIP):
    try:
        print(f"{BRIGHT_BLUE}[DEBUG] Starting connection function{RESET}")

        if inet_conn() == 0:
            print(f"{BRIGHT_BLUE}[DEBUG] Internet connection verified{RESET}")

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
    
            print(f"{BRIGHT_BLUE}[DEBUG] Modifying IP if necessary{RESET}")
            uIP = ip_chg(ip=uIP)
            print(f"IP CHANGE : {uIP}")
    
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
        print(f"{BRIGHT_BLUE}[DEBUG] Parsing command-line arguments{RESET}")

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
        parser.add_argument("-f", type=str, metavar="WAF check", help="Web Application Firewall check")
        parser.add_argument("-w", type=str, metavar="Wayback", help="Wayback Machine")
        parser.add_argument("-x", type=str, metavar="XSS", help="XSS Attack Payload")
        parser.add_argument("-i", type=str, metavar="IP INFO", help="Get IP Information")
        parser.add_argument("-v", "--version", action="version", version=config.version, help="IPScanMaster")

        args = parser.parse_args()

        try:
            print(f"{BRIGHT_BLUE}[DEBUG] Initializing variables for argument processing{RESET}")
            uIP = None

    
            if args.m == "scan":
                print(f"{BRIGHT_BLUE}[DEBUG] Scan mode selected{RESET}")

                if args.u:
                    uIP = args.u

                elif args.s:
                    print(f"{BRIGHT_BLUE}[DEBUG] Enumerating subdomains{RESET}")
                    enumerate_subdomain(domain=args.s)
                    return None, args.s
                
                elif args.p:
                    print(f"{BRIGHT_BLUE}[DEBUG] Scanning ports{RESET}")
                    scan_ports(ip=args.p)
                    return None, args.p
                
                elif args.d:
                    print(f"{BRIGHT_BLUE}[DEBUG] Performing directory search{RESET}")
                    DirSearch.search(self=DirSearch, ip=args.d)

                elif args.f:
                    print(f"{BRIGHT_BLUE}[DEBUG] Checking WAF{RESET}")
                    check_waf(ip=args.f)
                    return None, args.f
                
                elif args.w:
                    print(f"{BRIGHT_BLUE}[DEBUG] Using Wayback Machine{RESET}")
                    wayback = Wayback(url=args.w)
                    wayback.getData()

                elif args.x:
                    print(f"{BRIGHT_BLUE}[DEBUG] Using XSS-Attack Machine{RESET}")
                    vulb = XSSAttack(url=args.x)
                    vulb.attack()

                elif args.r:
                    print(f"{BRIGHT_BLUE}[DEBUG] Performing reverse IP lookup{RESET}")
                    reverseIP(ip=args.r)
                    return None, args.r
                
                elif args.i:
                    print(f"{BRIGHT_BLUE}[DEBUG] Getting IP information{RESET}")
                    ipinfo(ip=args.i)
                    return None, args.i
                
                else:            
                    print(f"{BRIGHT_RED}[ERROR] No valid arguments provided for scan mode{RESET}")
                    parser.print_help()
                    exit(1)
    
            elif args.m == "attack":
                if args.u:
                    uIP = args.u
                    attacker = Attacking(IP=uIP)
                    attacker.run_commands()
                    exit(0)

                else:
                    print(f"{BRIGHT_RED}[ERROR] IP or DNS is required for attack mode{RESET}")
                    exit(1)

            else:
                print(f"{BRIGHT_RED}[ERROR] Invalid mode provided{RESET}")
                parser.print_help()
                exit(1)

            if uIP:
                uIP = uIP.replace("https://", "").replace("http://", "").rstrip("/")
            return uIP, None

        except ValueError as e:
            print(f"{BRIGHT_RED}[ERROR] Value Error: {e}. Path = {__file__}{RESET}")
            exit(1)

        except Exception as e:
            print(f"{BRIGHT_RED}[ERROR] Unexpected Error: {e}. Path = {__file__}{RESET}")
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
       pass

    except Exception as e:
        print(f"{BRIGHT_RED}[ERROR] Error: {e}{RESET}")

    finally:
        TimeZone.end_time()

        if uIP:
            ip_history(ip=uIP)
