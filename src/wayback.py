#!/usr/bin/env python3

try:
    import requests
except ImportError:
    requests = None
import json
from tools.color import *

class Wayback:
    def __init__(self, url, output_path=None):
        self.url = url
        self.api = "https://web.archive.org/cdx/search/cdx"
        self.output_path = output_path

    def getData(self):
        if requests is None:
            print(f"{BRIGHT_RED}requests is not installed. Install requirements.txt to use Wayback.{RESET}")
            return []
        try:
            response = requests.get(
                self.api,
                params={"url": self.url, "output": "json", "filter": "statuscode:200"},
                timeout=20,
            )
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
                    
                    if self.output_path:
                        with open(self.output_path, "w", encoding="utf-8") as f:
                            json.dump(results, f, indent=4)
                        print(f"{BRIGHT_GREEN}Saved archive results to {self.output_path}")
                    return results
                else:
                    print(f"{BRIGHT_RED}No archived versions found.")
                    return []
            else:
                print(f"{BRIGHT_RED}Failed to fetch data.")
                return []

        except requests.exceptions.RequestException as e:
            print(f"{BRIGHT_RED}An error occurred: {e}")
            return []
        except IOError as e:
            print(f"{BRIGHT_RED}An error occurred while writing to file: {e}")
            return []
