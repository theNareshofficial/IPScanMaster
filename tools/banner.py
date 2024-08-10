#!/usr/bin/env python3

from tools.color import *
from tools.core import config

class Info:
    @classmethod
    def banner(cls):
        __banner__ = f"""{BOLD}{BRIGHT_GREEN}

              .:------::.                         
           :=====-----====-:                    
         :===:.         .:-===.                    
        ===:               .-==:                   
      -==.                   -==.                 
      :==:    IPScan          -==. 
      -==.        Master🔍     ===                  
       ===.                    -==:                  
      :==:                     ===                  
       ===                  :==-                  
       .===.               :==-                   
        .===-.          .:====                    
          :-===-::::::--====**=.                  
            .:-========-:.  .+*+++=:              
                              ++++++=:            
                              :=++++++=:          
                                :=++++++=:        
                                  :=++++++=:      
                                    :=+++++=      
                                      :===-  

            |  {BRIGHT_RED}{config.Author}{BLUE}
            |  {BRIGHT_RED}{config.Github}{BLUE}
            |  {BRIGHT_RED}{config.Youtube}{BLUE}

                                   {config.version}
            {config.description}

{RESET}"""
        print(__banner__)

# Call the class method to print the banner
Info.banner()
