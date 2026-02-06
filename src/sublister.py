#!/usr/bin/env python3

import sublist3r
from tools.color import *

def enumerate_subdomain(domain):
    try:
        subdomains = sublist3r.main(domain, 30, savefile=None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
        count = 0
        for subdomain in subdomains:
            print(f"{BRIGHT_MAGENTA}[+] {BRIGHT_CYAN}{subdomain}")
            count += 1
        print(f"\n\t {BRIGHT_MAGENTA}[+] {BRIGHT_CYAN} {count} Subdomain's Founded...")

    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Operation interrupted by user.")

if __name__ == "__main__":
    enumerate_subdomain()
