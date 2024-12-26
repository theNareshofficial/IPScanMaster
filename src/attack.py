#!/usr/bin/env python3

import subprocess
import datetime
import os
from tools.color import *
from src.ports import *
from src.reverse import *
from src.wayback import *

class Attacking:
    def __init__(self, IP=None):
        if not IP:
            raise ValueError(f"{BRIGHT_RED}IP address or domain is required.{RESET}")
        self.IP = IP
        # Timestamp for unique output folder names
        self.timestamp = datetime.datetime.now().strftime("%d%B%Y_%H%M%S")
        self.output_path = f"output/{self.IP}_{self.timestamp}"

    def create_output_dir(self):
        # Create the output directory if it does not exist
        os.makedirs(self.output_path, exist_ok=True)

    def run_commands(self):
        try:
            self.create_output_dir()

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Checking Your Original IP ----------[+]{RESET}{BRIGHT_GREEN}\n")
            reverseIP(ip=self.IP)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Open Port Scan ----------[+]{RESET}{BRIGHT_GREEN}\n")
            scan_ports(ip=self.IP)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- SubDomain Enumeration ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo subfinder -d {self.IP} -o {self.output_path}/subdomains.txt", shell=True, check=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- HTTPX-Toolkit ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo httpx-toolkit -l {self.output_path}/subdomains.txt -o {self.output_path}/https.txt", shell=True, check=True)
            subprocess.run(f"wc -l {self.output_path}/https.txt", shell=True, check=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- WAFW00F Check ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo wafw00f -i {self.output_path}/https.txt -o {self.output_path}/waf.txt", shell=True, check=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Wayback Check ----------[+]{RESET}{BRIGHT_GREEN}\n")
            wayback_instance = Wayback(url=self.IP, output_path=f"{self.output_path}/wayback.json")
            wayback_instance.getData()

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Directory Search ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo dirsearch -u {self.IP} -w injection/dirb_common.txt -o {self.output_path}/dirsearch.txt", shell=True, check=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- NMAP Whois-Domain ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo nmap --script whois-domain.nse {self.IP} -oN {self.output_path}/whois_Domain.txt", shell=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- NMAP Whois-IP ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo nmap {self.IP} --script whois-ip -o {self.output_path}/whois_IP.txt", shell=True, check=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- NMAP Vulners ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subprocess.run(f"sudo nmap -sV --script vulners {self.IP} -oN {self.output_path}/Vulners.txt", shell=True, check=True)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Completed ----------[+]{RESET}{BRIGHT_GREEN}\n")

            # Display saved files
            for filename in os.listdir(self.output_path):
                print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_CYAN} Saved: {self.output_path}/{filename}")

        except subprocess.CalledProcessError as e:
            print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_RED} Error executing command: {e}")
        except Exception as e:
            print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_RED} An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        ip_address = input("Enter the IP or domain: ").strip()
        attacker = Attacking(IP=ip_address)
        attacker.run_commands()
    except ValueError as ve:
        print(ve)
    except KeyboardInterrupt:
        print(f"\n{BRIGHT_RED}Execution interrupted by user.{RESET}")
    except Exception as e:
        print(f"\n{BRIGHT_RED}Unexpected Error: {e}{RESET}")
