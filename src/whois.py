#!/usr/bin/env python

import subprocess

def check_whois(ip):

            command = ["whois", ip]

            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.returncode == 0:
                    print(result.stdout)
                    return 0
            else:
                    print(f"{ip} Whois Not found!!!")
                    return 1
            
if __name__ == "__main__":
        check_whois()