#!/usr/bin/env python3

import subprocess

class DirSearch:

        def search(self, ip=None):
                self.ip = ip
                try:
                        subprocess.run(f"sudo dirsearch -u {self.ip} -w injection/dirb_small.txt", shell=True, check=True)
                except subprocess.SubprocessError as dir_error:
                        print(f"DirSearch : {dir_error}")

if __name__ == "__main__":
        DirSearch()