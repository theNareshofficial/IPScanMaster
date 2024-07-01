#!/usr/bin/env bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

check_root() {
    if sudo -n true 2>/dev/null; then
        echo "Sudo Mode"
        return 0
    else
        return 1
    fi
}

check_inet() {
    if ping -c 1 8.8.8.8 &>/dev/null; then
        echo "Internet Connection Successful..."
        return 0
    else
        echo "Internet Connection Failed!!!"
        return 1
    fi
}

check_python() {
    if command_exists python3; then
        echo "Python Found..."
        return 0
    else
            
            echo "Python3 Not Found"
            echo "Python3 Installing..."
            sudo apt install python3 -y &>/dev/null
            echo "Python3 Installtion Completed"
            return 1
    fi
}

check_git() {
            if command_exists git; then
                        echo "Git Found"
                        return 0
            else
                        echo "Git Not Found"
                        echo "Git Installing..."
                        sudo apt install git -y &>/dev/null
                        echo "Git Installtion Completed"
                        return 1
            fi
}

check_wafw00f() {

            if command_exists wafw00f; then
                        echo "Wafw00f Found"
            else
                        echo "Wafw00f Not Found"
                        echo "Wafw00f Installing..."
                        sudo apt install wafw00f -y &>/dev/null
                        echo "Wafw00f Installtion Completed"
}

if check_root; then
    check_inet
    check_python
    check_git
    check_wafw00f
else
    echo "Please run this script with sudo"
    exit 1
fi
