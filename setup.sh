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

                            IPScanMaster : v1.7
    ...A Tool for Gathering Detailed Information about IPs and Domains...
"""

}
bannner

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

check_root() {
    if sudo -n true 2>/dev/null; then
        return 0
    else
        echo "Please run this script with sudo!!!"
        return 1
    fi
}

check_inet() {
    if ping -c 1 8.8.8.8 &>/dev/null; then
        echo "[+]---------- Internet Connection Successful ----------[+]"
        return 0
    else
        echo "[+]---------- Internet Connection Failed ----------[+]"
        return 1
    fi
}

check_update() {
    echo "[+]---------- Updating ----------[+]"
    sudo apt update -y &>/dev/null
    echo "[+]---------- Upgrading ----------[+]"
    sudo apt upgrade -y &>/dev/null
    echo "[+]---------- Update Completed ----------[+]"
}

check_python() {
    if command_exists python3; then
        echo "[+]---------- Python Found ----------[+]"
        return 0
    else
        echo "[+]---------- Python3 Not Found ----------[+]"
        echo "Python3 Installing..."
        sudo apt install python3 -y &>/dev/null
        echo "Python3 Installation Completed"
        return 1
    fi
}

check_git() {
    if command_exists git; then
        echo "[+]---------- Git Found ----------[+]"
        return 0
    else
        echo "[+]---------- Git Not Found ----------[+]"
        echo "Git Installing..."
        sudo apt install git -y &>/dev/null
        echo "Git Installation Completed"
        return 1
    fi
}

check_wafw00f() {
    if command_exists wafw00f; then
        echo "[+]---------- Wafw00f Found ----------[+]"
    else
        echo "[+]---------- Wafw00f Not Found ----------[+]"
        echo "Wafw00f Installing..."
        sudo apt install wafw00f -y &>/dev/null
        echo "Wafw00f Installation Completed"
    fi
}

install_requirements() {
    echo "[+]---------- Installing Python requirements ----------[+]"
    pip install -r requirements.txt &>/dev/null
    echo "Python requirements installation completed"
}


if check_root && check_inet; then
    check_update
    check_python
    check_git
    check_wafw00f
    install_requirements
    exit 0
else
    exit 1
fi
