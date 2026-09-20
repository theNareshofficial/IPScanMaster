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

def print_section(title, icon="⚡"):
    """Prints a sleek, uniform UTF-8 section header matching the framework style."""
    print(f"\n{BRIGHT_CYAN}╭─────────────────────────────────────────────────────────╮{RESET}")
    print(f"{BRIGHT_CYAN}│{RESET} {BRIGHT_GREEN}{icon} {title:<51}{RESET} {BRIGHT_CYAN}│{RESET}")
    print(f"{BRIGHT_CYAN}╰─────────────────────────────────────────────────────────╯{RESET}\n")

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
            print(f"{BRIGHT_RED}✖ {command[0]} is not installed or not on PATH; skipping this step.{RESET}")
            return False
        try:
            subprocess.run(command, check=True)
            return True
        except subprocess.CalledProcessError as error:
            print(f"{BRIGHT_RED}✖ Command failed: {error}{RESET}")
            return False

    def run_commands(self):
        try:
            self.create_output_dir()

            print_section("Checking Your Original IP", icon="🔍")
            reverseIP(ip=self.IP)

            print_section("Open Port Scan", icon="🔌")
            scan_ports(ip=self.IP)

            print_section("SubDomain Enumeration", icon="📂")
            subdomains_path = os.path.join(self.output_path, "subdomains.txt")
            self.run_tool(["subfinder", "-d", self.IP, "-o", subdomains_path])

            print_section("HTTPX-Toolkit", icon="🌐")
            https_path = os.path.join(self.output_path, "https.txt")
            if os.path.exists(subdomains_path):
                self.run_tool(["httpx-toolkit", "-l", subdomains_path, "-o", https_path])

            print_section("WAFW00F Check", icon="🛡️")
            if os.path.exists(https_path):
                self.run_tool(["wafw00f", "-i", https_path, "-o", os.path.join(self.output_path, "waf.txt")])

            print_section("Wayback Check", icon="⏳")
            wayback_instance = Wayback(url=self.IP, output_path=f"{self.output_path}/wayback.json")
            wayback_instance.getData()

            print_section("Directory Search", icon="📁")
            target = self.IP if "://" in self.IP else f"https://{self.IP}"
            self.run_tool(["dirsearch", "-u", target, "-w", "injection/dirb/dirb_common.txt", "-o", os.path.join(self.output_path, "dirsearch.txt")])

            print_section("NMAP Whois-Domain", icon="📋")
            self.run_tool(["nmap", "--script", "whois-domain.nse", self.IP, "-oN", os.path.join(self.output_path, "whois_Domain.txt")])

            print_section("NMAP Whois-IP", icon="🌍")
            self.run_tool(["nmap", self.IP, "--script", "whois-ip", "-oN", os.path.join(self.output_path, "whois_IP.txt")])

            print_section("NMAP Vulners", icon="⚡")
            self.run_tool(["nmap", "-sV", "--script", "vulners", self.IP, "-oN", os.path.join(self.output_path, "Vulners.txt")])

            print(f"\n{BRIGHT_GREEN}✨ [+]---------- Completed ----------[+]{RESET}\n")

            # Display saved files with clean icons
            for filename in os.listdir(self.output_path):
                print(f"{BRIGHT_MAGENTA}[💾]{BRIGHT_CYAN} Saved: {self.output_path}/{filename}")

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