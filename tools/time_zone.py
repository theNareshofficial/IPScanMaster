#!/usr/bin/env python3

import datetime
from tools.color import *

class TimeZone:

    @staticmethod
    def start_time():
        start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{BRIGHT_MAGENTA}[+] {BRIGHT_CYAN}Started : {start}")

    @staticmethod
    def end_time():
        end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{BRIGHT_MAGENTA}[+] {BRIGHT_CYAN}Finished : {end}")

if __name__ == "__main__":
    TimeZone()
