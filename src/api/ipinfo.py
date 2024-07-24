#!/usr/bin/env python3

import requests
from tools.color import *

def get_ip_location(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f" [+] Error fetching IP location: {e}")
        return None

def ipinfo(ip):
    location_info = get_ip_location(ip)

    if location_info:
        print(f" \n {BRIGHT_MAGENTA} [+]{BRIGHT_CYAN} IP Location Information:")
        print(f" {BRIGHT_MAGENTA} [+]{BRIGHT_CYAN} IP: {location_info.get('ip')}")
        print(f" {BRIGHT_MAGENTA} [+]{BRIGHT_CYAN} City: {location_info.get('city')}")
        print(f" {BRIGHT_MAGENTA} [+]{BRIGHT_CYAN} Region: {location_info.get('region')}")
        print(f" {BRIGHT_MAGENTA} [+]{BRIGHT_CYAN} Country: {location_info.get('country')}")
        print(f" {BRIGHT_MAGENTA} [+]{BRIGHT_CYAN} Location: {location_info.get('loc')}")
        print(f" {BRIGHT_MAGENTA} [+]{BRIGHT_CYAN} Organization: {location_info.get('org')}")
        print(f" {BRIGHT_MAGENTA} [+]{BRIGHT_CYAN} Timezone: {location_info.get('timezone')}")
    else:
        print("Unable to retrieve IP location.")

if __name__ == "__main__":
    ipinfo()
