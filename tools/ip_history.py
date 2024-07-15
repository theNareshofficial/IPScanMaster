#!/usr/bin/env python

import datetime

def ip_history(ip):
            
            try:
                 date_string = "15-07-2024 : 14:30:45"
                 dt = datetime.datetime.strptime(date_string, "%d-%m-%Y : %H:%M:%S")
                 with open("history", "a") as file:
                       file.write(f"{ip} {dt}\n")
                       file.close()
            except FileNotFoundError:
                    print("File Not Found!!!")
            except KeyboardInterrupt:
                    pass        
            except Exception as e:
                    print(f"{e}") 

if __name__ == "__main__":
        ip_history()   
                
