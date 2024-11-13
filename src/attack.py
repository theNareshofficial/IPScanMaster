#!/usr/bin/env python3

import subprocess
import datetime
from tools.color import *
from src.ports import *
from src.reverse import *

class Attacking:

    def __init__(self, IP=None):
        self.IP = IP

    def run_commands(self):
        try:

            dt = datetime.datetime.now().strftime("%d:%B:%Y_%H:%M:%S")
            path = (f"{self.IP}_{dt}")

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Checking Your Original IP ----------[+]{RESET}{BRIGHT_GREEN}\n")
            self.IP = reverseIP(ip=self.IP)
            print(f"Original IP : {self.IP}")

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Open Port Scan ----------[+]{RESET}{BRIGHT_GREEN}\n")
            scan_ports(ip=self.IP)
    
            print(f"\n{BRIGHT_MAGENTA}[+]---------- SubDomain Enumeration ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo subfinder -d {self.IP} -o output/{path}/subdomains.txt", shell=True, check=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- HTTPX-Toolkit ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo httpx-toolkit -l output/{path}/subdomains.txt -o output/{path}/https.txt", shell=True, check=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- WAFW00F Check ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo wafw00f -i output/{path}/https.txt -o output/{path}/waf.txt", shell=True, check=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Directory Search ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo dirsearch -u {self.IP} -w injection/dirb_common.txt -o output/{path}/dirsearch.txt", shell=True, check=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- NMAP Whois-Domain ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo nmap --script whois-domain.nse {self.IP} -oN output/{path}/whois_Domain.txt", shell=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- NMAP Whois-IP ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo nmap {self.IP} --script whois-ip -o output/{path}/whois_IP.txt", shell=True, check=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- NMAP Vulners ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo nmap -sV --script vulners {self.IP} -oN output/{path}/Vulners.txt", shell=True, check=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Completed ----------[+]{BRIGHT_GREEN}\n")

            print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_CYAN} Saved output/{path}/subdomains.txt")
            print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_CYAN} Saved output/{path}/https.txt")
            print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_CYAN} Saved output/{path}/waf.txt")
            print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_CYAN} Saved output/{path}/whois_IP.txt")
            print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_CYAN} Saved output/{path}/whois_Domain.txt")
            print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_CYAN} Saved output/{path}/Vulners.txt")

        except subprocess.CalledProcessError as e:
            print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_RED} Error executing command: {e}")


if __name__ == "__main__":
    attcker = Attacking()
    attcker.run_commands()