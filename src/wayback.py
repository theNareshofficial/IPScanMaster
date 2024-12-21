#!/usr/bin/env python3

import requests

class Wayback:
    def __init__(self, url):
        self.url = url
        self.api = f"http://web.archive.org/cdx/search/cdx?url={self.url}&output=json"

    def getData(self):
        try:
            response = requests.get(self.api)
            response.raise_for_status()

            if response.ok:
                data = response.json()
                if data:
                    print("Archived Versions:")
                    for entry in data[1:]:  # Skip the header row
                        print(f"Timestamp: {entry[1]}, Archive URL: https://web.archive.org/web/{entry[1]}/{entry[2]}")
                else:
                    print("No archived versions found.")
            else:
                print("Failed to fetch data.")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
