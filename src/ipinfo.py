#!/usr/bin/env python

import requests

def get_ip_location(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching IP location: {e}")
        return None

def ipinfo(ip):
    location_info = get_ip_location(ip)

    if location_info:
        print(f"\nIP Location Information:")
        print(f"IP: {location_info.get('ip')}")
        print(f"City: {location_info.get('city')}")
        print(f"Region: {location_info.get('region')}")
        print(f"Country: {location_info.get('country')}")
        print(f"Location: {location_info.get('loc')}")
        print(f"Organization: {location_info.get('org')}")
        print(f"Timezone: {location_info.get('timezone')}")
    else:
        print("Unable to retrieve IP location.")

if __name__ == "__main__":
    ipinfo()
