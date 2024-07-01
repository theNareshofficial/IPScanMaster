#!/usr/bin/env python


import os

def clrscr():

            os_name = os.name

            if os_name  == 'nt':
                    os.system("cls")            # Windows
            else:
                    os.system("clear")          # Linux/MacOS

if __name__ == "__main__":
        clrscr()
