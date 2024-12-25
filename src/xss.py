#!/usr/bin/env python3

import requests
from tools.color import *

class XSSAttack:
    def __init__(self, url=None):
        self.url = url

    def load_payloads(self, filepath):
        """Load payloads from a file."""
        try:
            with open(filepath, "r") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"{BRIGHT_RED}[ERROR] File not found: {filepath}")
            return []

    def attack(self):
        """Perform the XSS attack."""
        if not self.url:
            print(f"{BRIGHT_RED}[ERROR] No URL provided. Exiting.")
            return

        payload_file = './injection/payload/XSS-payloadbox.txt'

        payloads = self.load_payloads(payload_file)

        if not payloads:
            print(f"{BRIGHT_RED}[ERROR] No payloads loaded. Exiting.")
            return

        for payload in payloads:
            params = {"q": payload}

            try:
                response = requests.get(self.url, params=params)

                if payload in response.text:
                    print(f"{BRIGHT_MAGENTA}[Vulnerable] --> {BRIGHT_CYAN}{self.url} --> {BRIGHT_GREEN}{payload}")
                else:
                    print(f"{BRIGHT_RED}[NOT Vulnerable] --> {BRIGHT_CYAN}{self.url} --> {BRIGHT_GREEN}{payload}")

            except requests.exceptions.RequestException as e:
                print(f"[ERROR] Request failed: {e}")
            except KeyboardInterrupt:
                print("\n[INFO] Process interrupted by user. Exiting.")
                return
