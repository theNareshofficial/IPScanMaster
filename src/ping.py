#!/usr/bin/env python3

import os
import subprocess
from tools.color import *

def ip_Reachable(ip):

            try:
                        os_name = os.name

                        if os_name == "nt":
                                    command = ["ping", "-n", "1", ip]
                        else:
                                    command = ["ping", "-c", "1", ip]

                        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                        if result.returncode == 0:
                                    print(f"{MAGENTA} [+] {CYAN}{ip} is Reachable...")
                                    return 0
                        else:
                                    print(f"{MAGENTA} [!] {RED}{ip} is not Reachable!!!")
                                    exit()
            except Exception as ping_error:
                    print(f"{MAGENTA} [!] {RED}{ping_error}, path={__path__}")
            except KeyboardInterrupt:
                    pass
            
if __name__ == "__main__":
        ip_Reachable()