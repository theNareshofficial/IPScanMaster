#!/usr/bin/env bash


bannner() {

echo """
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

          |  Author  : Naresh
          |  Github  : https://github.com/theNareshofficial
          |  Youtube : https://www.youtube.com/@nareshtechweb930    

                            IPScanMaster : v2.07
    ...A Tool for Gathering Detailed Information about IPs and Domains...
"""

}
clear
bannner

echo Hello, $(whoami)

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

check_root() {
    if sudo -n true 2>/dev/null; then
        return 0
    else
        echo "[+] Please run this script with sudo!!!"
        return 1
    fi
}

check_inet() {
    if ping -c 1 8.8.8.8 &>/dev/null; then
        echo "[+]---------->> Internet Connection Successful"
        return 0
    else
        echo "[!]---------->> Internet Connection Failed"
        return 1
    fi
}

check_python() {
    if command_exists python3; then
        echo "[+]---------->> Python3 Found"
        return 0
    else
        echo "[!]---------->> Python3 Not Found"
        echo "[~]Python3 Installing..."
        sudo apt install python3 -y &>/dev/null
        sudo apt install python3-pip -y &>/dev/null
        echo "[+]Python3 Installation Completed"
        return 1
    fi
}

check_wafw00f() {
    if command_exists wafw00f; then
        echo "[+]---------->> Wafw00f Found"
    else
        echo "[!]---------->> Wafw00f Not Found"
        echo "[~]Wafw00f Installing..."
        sudo apt install wafw00f -y &>/dev/null
        echo "[+]Wafw00f Installation Completed"
    fi
}

check_subfinder() {
    if command_exists subfinder; then
        echo "[+]---------->> subfinder Found"
    else
        echo "[+]---------->> subfinder Not Found"
        echo "[~]---------->> subfinder Installting..."
        sudo apt install subfinder -y &>/dev/null
        echo "[+]subfinder Installation Completed"
    fi

}

check_httpx() {
    if command_exists httpx-toolkit; then
        echo "[+]---------->> httpx-toolkit Found"
    else
        echo "[+]---------->> httpx-toolkit Not Found"
        echo "[~]---------->> httpx-toolkit Installting..."
        sudo apt install httpx-toolkit -y &>/dev/null
        echo "[+]httpx-toolkit Installation Completed"
    fi

}

check_dirSearch() {
    if command_exists dirsearch; then
        echo "[+]---------->> dirsearch Found"
    else
        echo "[+]---------->> dirsearch Not Found"
        echo "[~]---------->> dirsearch Installting..."
        sudo apt install dirsearch -y &>/dev/null
        echo "[+]dirsearch Installation Completed"
    fi

}

check_nmap() {
    if command_exists nmap; then
        echo "[+]---------->> NMAP Found"
    else
        echo "[+]---------->> NMAP Not Found"
        echo "[~]---------->> NMAP Installting..."
        sudo apt install NMAP -y &>/dev/null
        echo "[+]NMAP Installation Completed"
    fi

}

install_requirements() {
    echo "[+]---------->> Installing Python requirements"
    pip install -r requirements.txt &>/dev/null
    echo "[+] Python requirements installation completed."
}


if check_root && check_inet; then
    check_python
    check_wafw00f
    check_dirSearch
    check_nmap
    check_subfinder
    check_httpx
    install_requirements
    exit 0
else
    exit 1
fi
