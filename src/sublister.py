#!/usr/bin/env python3

try:
    import sublist3r
except ImportError:
    sublist3r = None
from tools.color import *

def enumerate_subdomain(domain):
    if sublist3r is None:
        print(f"{BRIGHT_RED}Sublist3r is not installed. Install requirements.txt to enumerate subdomains.{RESET}")
        return []
    try:
        subdomains = sublist3r.main(domain, 30, savefile=None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
        count = 0
        for subdomain in subdomains:
            print(f"{BRIGHT_MAGENTA}[+] {BRIGHT_CYAN}{subdomain}")
            count += 1
        print(f"\n\t {BRIGHT_MAGENTA}[+] {BRIGHT_CYAN} {count} Subdomain's Founded...")
        return subdomains

    except Exception as e:
        print(f"Error: {e}")
        return []
    except KeyboardInterrupt:
        print("Operation interrupted by user.")

if __name__ == "__main__":
    enumerate_subdomain()
