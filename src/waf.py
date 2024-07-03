#!/usr/bin/env python

import wafw00f
import wafw00f.main
from urllib.parse import urlparse

def check_waf(ip):

            try:
                    if not urlparse(ip).scheme:
                           ip = "https://" + ip

                    waf = wafw00f.main.WAFW00F(ip)      
                    results = waf.identwaf()

                    if results:
                                print(f"WAF is detected {ip}")
                                for waf_name in results:
                                        print(f" - {waf_name}")
                    else:
                                print(f"No WAF is detected!!!")

            except KeyboardInterrupt:
                    pass

if __name__ == "__main__":
        check_waf()
