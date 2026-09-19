#!/usr/bin/env python3

try:
    import wafw00f.main
except ImportError:
    wafw00f = None
from urllib.parse import urlparse
from tools.color import *

def check_waf(ip):
            if wafw00f is None:
                    print(f"{BRIGHT_RED}wafw00f is not installed. Install requirements.txt to enable WAF detection.{RESET}")
                    return 1
            try:
                    if not urlparse(ip).scheme:
                           ip = "https://" + ip

                    waf = wafw00f.main.WAFW00F(ip)      
                    results = waf.identwaf()

                    if results:
                                print(f"{BRIGHT_MAGENTA}[+] {BRIGHT_CYAN}WAF is detected {ip}")
                                for waf_name in results:
                                        print(f"\t {BRIGHT_MAGENTA}- {BRIGHT_CYAN}{waf_name}")
                    else:
                                print(f" {BRIGHT_MAGENTA} [+] {BRIGHT_RED} No WAF is detected!!!")
                    return 0
            except Exception as waf_error:
                    print(waf_error)    
                    return 1
            except KeyboardInterrupt:
                    pass

if __name__ == "__main__":
        check_waf()
