#!/usr/bin/env python3

import wafw00f
import wafw00f.main
from urllib.parse import urlparse
from tools.color import *

def check_waf(ip):

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
            except Exception as waf_error:
                    print(waf_error)    
            except KeyboardInterrupt:
                    pass

if __name__ == "__main__":
        check_waf()
