#!/usr/bin/env python3

import datetime

def ip_history(ip):
            
            try:
                 dt = datetime.datetime.now().strftime("%d-%m-%Y : %H:%M:%S")
                 with open("history", "a") as file:
                       file.write(f"{ip} {dt}\n")
                       print("[+] IP Saved in history file...")
                       file.close()
            except FileNotFoundError:
                    print("File Not Found!!!")
            except KeyboardInterrupt:
                    pass        
            except Exception as e:
                    print(f"{e}") 

if __name__ == "__main__":
        ip_history()   
                
