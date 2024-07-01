#!/usr/bin/env python

import os
import subprocess

def ip_Reachable(ip):

            try:
                        os_name = os.name

                        if os_name == "nt":
                                    command = ["ping", "-n", "1", ip]
                        else:
                                    command = ["ping", "-c", "1", ip]

                        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                        if result.returncode == 0:
                                    print(f"{ip} is Reachable...")
                                    return 0
                        else:
                                    print(f"{ip} is not Reachable!!!")
                                    return 1
            
            except KeyboardInterrupt:
                    pass
            
if __name__ == "__main__":
        ip = input("Enter Your IP : ")
        ip_Reachable(ip)