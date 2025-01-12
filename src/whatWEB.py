#!/usr/bin/env python3

import subprocess
from tools.color import *

class WhatWeb:

            def ScanWeb(self, url=None):
                    self.url = url

                    if not self.url:
                        print("[!] URL is EMPTY !!!")
                        return

                    CMD = ['sudo', 'whatweb', self.url]

                    result = subprocess.run(CMD, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                    if result.returncode == 0:
                        #print("Scan Successfully")
                        print(f"{BRIGHT_MAGENTA}[+]{BRIGHT_CYAN} {result.stdout}")
                    elif result.returncode == 1:
                        # print("Scan Failed")    
                        print(f"{BRIGHT_MAGENTA}[!]{BRIGHT_RED} {result.stderr}")
                    else:
                        exit
