#!/usr/bin/env python3

from tools.color import *
import subprocess

def enumerate_subdomain(domain):
    # print(f"{BRIGHT_YELLOW}[*] Enumerating subdomains for: {domain} using Subfinder...")
    try:
        command = ["subfinder", "-d", domain, "-silent"]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
    
            subdomains = result.stdout.strip().splitlines()
            
            count = 0
            for subdomain in subdomains:
                print(f"{BRIGHT_MAGENTA}[+] {BRIGHT_CYAN}{subdomain}")
                count += 1
            
            print(f"\n\t {BRIGHT_MAGENTA}[+] {BRIGHT_CYAN} {count} Subdomain's Founded...")
        else:
            print(f"{BRIGHT_RED}Error running Subfinder: {result.stderr}{RESET}")

    except FileNotFoundError:
        print(f"{BRIGHT_RED}Error: Subfinder is not installed or not in your PATH.{RESET}")
    except Exception as e:
        print(f"{BRIGHT_RED}Error: {e}{RESET}")
    except KeyboardInterrupt:
        print(f"\n{BRIGHT_YELLOW}Operation interrupted by user.{RESET}")

if __name__ == "__main__":
    target_domain = input(f"{BRIGHT_GREEN}Enter Domain (e.g. google.com): {RESET}")
    if target_domain:
        enumerate_subdomain(target_domain)
    else:
        print(f"{BRIGHT_RED}No domain entered. Exiting.{RESET}")