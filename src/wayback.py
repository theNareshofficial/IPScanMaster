#!/usr/bin/env python3

import requests
import json
from tools.color import *

class Wayback:
    def __init__(self, url, output_path=str(None)):
        self.url = url
        self.api = f"http://web.archive.org/cdx/search/cdx?url={self.url}&output=json"
        self.output_path = output_path

    def getData(self):
        try:
            response = requests.get(self.api)
            response.raise_for_status()

            if response.ok:
                data = response.json()
                
                if data:
                    print(f"{BRIGHT_GREEN}Archived Versions:")
                    results = []
                    for entry in data[1:]:  # Skip the header row
                        archive_url = f"https://web.archive.org/web/{entry[1]}/{entry[2]}"
                        print(f"{BRIGHT_MAGENTA}Timestamp: {entry[1]}, Archive URL: {BRIGHT_CYAN}{archive_url}")
                        results.append({"timestamp": entry[1], "archive_url": archive_url})
                    
                    # Save the results to the specified file
                    with open(self.output_path, "w") as f:
                        json.dump(results, f, indent=4)
                else:
                    print(f"{BRIGHT_RED}No archived versions found.")
            else:
                print("{BRIGHT_RED}Failed to fetch data.")

        except requests.exceptions.RequestException as e:
            print(f"{BRIGHT_RED}An error occurred: {e}")
        except IOError as e:
            print(f"{BRIGHT_RED}An error occurred while writing to file: {e}")
