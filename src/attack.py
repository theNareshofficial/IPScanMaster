#!/usr/bin/env python3

import subprocess
import datetime
import os
import re
import shutil
from tools.color import *
from src.ports import *
from src.reverse import *
from src.wayback import *

class Attacking:
    def __init__(self, IP=None):
        if not IP:
            raise ValueError(f"{BRIGHT_RED}IP address or domain is required {RESET}")
        self.IP = IP
        # Timestamp for unique output folder names
        self.timestamp = datetime.datetime.now().strftime("%d%B%Y_%H%M%S")
        safe_target = re.sub(r"[^A-Za-z0-9.-]", "_", IP)
        self.output_path = os.path.join("output", f"{safe_target}_{self.timestamp}")
 
    def create_output_dir(self):
        os.makedirs(self.output_path, exist_ok=True)

    @staticmethod
    def run_tool(command):

        if not shutil.which(command[0]):
            print(f"{BRIGHT_RED}{command[0]} is not installed or not on PATH; skipping this step.{RESET}")
            return False
        try:
            subprocess.run(command, check=True)
            return True
        except subprocess.CalledProcessError as error:
            print(f"{BRIGHT_RED}Command failed: {error}{RESET}")
            return False

    def run_commands(self):
        try:
            self.create_output_dir()

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Checking Your Original IP ----------[+]{RESET}{BRIGHT_GREEN}\n")
            reverseIP(ip=self.IP)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Open Port Scan ----------[+]{RESET}{BRIGHT_GREEN}\n")
            scan_ports(ip=self.IP)

            print(f"\n{BRIGHT_MAGENTA}[+]---------- SubDomain Enumeration ----------[+]{RESET}{BRIGHT_GREEN}\n")
            subdomains_path = os.path.join(self.output_path, "subdomains.txt")
            self.run_tool(["subfinder", "-d", self.IP, "-o", subdomains_path])

            print(f"\n{BRIGHT_MAGENTA}[+]---------- HTTPX-Toolkit ----------[+]{RESET}{BRIGHT_GREEN}\n")
            https_path = os.path.join(self.output_path, "https.txt")
            if os.path.exists(subdomains_path):
                self.run_tool(["httpx-toolkit", "-l", subdomains_path, "-o", https_path])

            print(f"\n{BRIGHT_MAGENTA}[+]---------- WAFW00F Check ----------[+]{RESET}{BRIGHT_GREEN}\n")
            if os.path.exists(https_path):
                self.run_tool(["wafw00f", "-i", https_path, "-o", os.path.join(self.output_path, "waf.txt")])

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Wayback Check ----------[+]{RESET}{BRIGHT_GREEN}\n")
            wayback_instance = Wayback(url=self.IP, output_path=f"{self.output_path}/wayback.json")
            wayback_instance.getData()

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Directory Search ----------[+]{RESET}{BRIGHT_GREEN}\n")
            target = self.IP if "://" in self.IP else f"https://{self.IP}"
            self.run_tool(["dirsearch", "-u", target, "-w", "injection/dirb/dirb_common.txt", "-o", os.path.join(self.output_path, "dirsearch.txt")])

            print(f"\n{BRIGHT_MAGENTA}[+]---------- NMAP Whois-Domain ----------[+]{RESET}{BRIGHT_GREEN}\n")
            self.run_tool(["nmap", "--script", "whois-domain.nse", self.IP, "-oN", os.path.join(self.output_path, "whois_Domain.txt")])

            print(f"\n{BRIGHT_MAGENTA}[+]---------- NMAP Whois-IP ----------[+]{RESET}{BRIGHT_GREEN}\n")
            self.run_tool(["nmap", self.IP, "--script", "whois-ip", "-oN", os.path.join(self.output_path, "whois_IP.txt")])

            print(f"\n{BRIGHT_MAGENTA}[+]---------- NMAP Vulners ----------[+]{RESET}{BRIGHT_GREEN}\n")
            self.run_tool(["nmap", "-sV", "--script", "vulners", self.IP, "-oN", os.path.join(self.output_path, "Vulners.txt")])

            print(f"\n{BRIGHT_MAGENTA}[+]---------- Completed ----------[+]{RESET}{BRIGHT_GREEN}\n")

            # Display saved files
            for filename in os.listdir(self.output_path):
                print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_CYAN} Saved: {self.output_path}/{filename}")

        except subprocess.CalledProcessError as e:
            print(f"{BRIGHT_MAGENTA}[❌]{BRIGHT_RED} Error executing command: {e}, PATH={__file__}")
        except Exception as e:
            print(f"{BRIGHT_MAGENTA}[❌]{BRIGHT_RED} An unexpected error occurred: {e}, PATH={__file__}")


if __name__ == "__main__":
    try:
        ip_address = input("Enter the IP or domain: ").strip()
        attacker = Attacking(IP=ip_address)
        attacker.run_commands()
    except ValueError as ve:
        print(f"{ve}, PATH={__file__}")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\n{BRIGHT_RED}Unexpected Error: {e}, PATH={__file__}{RESET}")
