#!/usr/bin/env python

# ANSI escape codes for colors
BOLD = '\033[1m'
RED = '\033[31m'
BLUE = '\033[34m'
RESET = '\033[0m'
GREEN = '\033[32m'

def banner():
    __banner__ = f"""{BOLD}{GREEN}

              .:------::.                         
           :=====-----====-:                    
         :===:.        .:-===.                    
        ===:              .-==:                   
      :==:                   ===                  
      -==.                    -==.                 
       ===.   IPScan         -==:                  
      :==:      Master🔍      ===                  
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

          |  {RED}Author  : Naresh{BLUE}
          |  {RED}Github  : https://github.com/theNareshofficial{BLUE}
          |  {RED}Youtube : https://www.youtube.com/@nareshtechweb930{BLUE}

                             IPScanMaster : v1.8
      ...A Tool for Gathering Detailed Information about IPs and Domains...

{RESET}"""
    print(__banner__)

banner()
