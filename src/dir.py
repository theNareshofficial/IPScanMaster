#!/usr/bin/env python3

import shutil
import subprocess

class DirSearch:

        def search(self, ip=None):
                if not ip:
                        print("DirSearch: a URL or domain is required.")
                        return 1
                if not shutil.which("dirsearch"):
                        print("DirSearch: 'dirsearch' is not installed or not on PATH.")
                        return 1
                target = ip if "://" in ip else f"https://{ip}"
                try:
                        subprocess.run(["dirsearch", "-u", target, "-w", "injection/dirb/dirb_small.txt"], check=True)
                        return 0
                except subprocess.SubprocessError as dir_error:
                        print(f"DirSearch : {dir_error}")
                        return 1

if __name__ == "__main__":
        DirSearch()
