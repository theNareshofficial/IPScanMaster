#!/usr/bin/env python

import os
import subprocess

def inet_conn(ip="8.8.8.8"):                  # Internet_Connection

            os_check = os.name

            if os_check == "nt":
                    
                    command = ["ping", "-n", "1", ip]
            else:
                    command = ["ping", "-c", "1", ip]

            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, )

            if result.returncode == 0:
                #     print("Internet Connection Successfully...")
                    return 0
            else:
                    print("Internet Connection Failed!!!") 
                    return 1
            
if __name__ == "__main__":
        inet_conn()