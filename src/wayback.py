#!/usr/bin/env python3

import requests
import json

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
                    print("Archived Versions:")
                    results = []
                    for entry in data[1:]:  # Skip the header row
                        archive_url = f"https://web.archive.org/web/{entry[1]}/{entry[2]}"
                        print(f"Timestamp: {entry[1]}, Archive URL: {archive_url}")
                        results.append({"timestamp": entry[1], "archive_url": archive_url})
                    
                    # Save the results to the specified file
                    with open(self.output_path, "w") as f:
                        json.dump(results, f, indent=4)
                    
            #         print(f"\nResults saved to {self.output_path}")
                else:
                    print("No archived versions found.")
            else:
                print("Failed to fetch data.")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        except IOError as e:
            print(f"An error occurred while writing to file: {e}")
