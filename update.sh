#!/usr/bin/env bash

echo Hello, $(whoami)


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

update() {
            echo "[+]----->> Updating Dirsearch..."
            sudo apt install --only-upgrade dirsearch
            echo "[+]----->> Updating wafw00f..."
            sudo apt install --only-upgrade wafw00f
            echo "[+]----->> Updating NMAP..."
            sudo apt install --only-upgrade nmap
            echo "[+]----->> Updating Subfinder..."
            sudo apt install --only-upgrade subfinder
            echo "[+]----->> Updating Python3..."
            sudo apt install --only-upgrade python3
            echo "[+]----->> Update Completed..."
}

if check_root && check_inet; then
            update
            exit 0
else
            exit 1
fi