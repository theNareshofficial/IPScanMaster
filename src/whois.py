#!/usr/bin/env python

import subprocess
import sys
import time
import threading

class Spinner:
    """A smooth UTF-8 terminal loading spinner thread."""
    def __init__(self, message="Fetching WHOIS data..."):
        self.spinner_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.message = message
        self.running = False
        self.thread = None

    def _spin(self):
        i = 0
        while self.running:
            sys.stdout.write(f"\r\033[1;36m{self.spinner_chars[i]}\033[0m {self.message}")
            sys.stdout.flush()
            i = (i + 1) % len(self.spinner_chars)
            time.sleep(0.08)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        # Clear the spinner line
        sys.stdout.write("\r\033[K")
        sys.stdout.flush()

def format_whois_output(raw_text):
    """Formats raw WHOIS text into a sleek UTF-8 box design."""
    lines = raw_text.splitlines()
    formatted_lines = []
    
    # Unicode box header
    formatted_lines.append("\033[1;36m╭─────────────────────────────────────────────────────────╮\033[0m")
    formatted_lines.append("\033[1;36m│\033[0m \033[1;32m🌐 WHOIS RECORD REPORT                            \033[1;36m│\033[0m")
    formatted_lines.append("\033[1;36m├─────────────────────────────────────────────────────────┤\033[0m")
    
    for line in lines:
        line_str = line.strip()
        # Skip comment or empty lines to keep design compact
        if not line_str or line_str.startswith("#") or line_str.startswith("%"):
            continue
            
        if ":" in line_str:
            parts = line_str.split(":", 1)
            key = parts[0].strip()
            val = parts[1].strip()
            formatted_lines.append(f"\033[1;36m│\033[0m  \033[1m{key:<20}\033[0m: {val}")
        else:
            formatted_lines.append(f"\033[1;36m│\033[0m  {line_str}")
            
    formatted_lines.append("\033[1;36m╰─────────────────────────────────────────────────────────╯\033[0m")
    return "\n".join(formatted_lines)

def check_whois(ip):
    command = ["whois", ip]
    
    # Start UTF-8 terminal spinner animation
    spinner = Spinner(message=f"Querying WHOIS for \033[1m{ip}\033[0m...")
    spinner.start()
    
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
    except FileNotFoundError:
        spinner.stop()
        print("\033[1;31m✖ Error: 'whois' is not installed or not on PATH.\033[0m")
        return 1
    except subprocess.TimeoutExpired:
        spinner.stop()
        print(f"\033[1;31m✖ Error: WHOIS lookup for {ip} timed out.\033[0m")
        return 1
    finally:
        spinner.stop()

    if result.returncode == 0:
        print(format_whois_output(result.stdout))
        return 0
        
    print(f"\033[1;33m⚠ {ip}: Whois Not found!!!\033[0m")
    return 1
            
if __name__ == "__main__":
    target_ip = sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8"
    check_whois(target_ip)