#!/usr/bin/python3

"""This script takes in a URL, sends a request to it,
and displays the body of the response"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    print(f"Error code: {response.status_code}" if response.status_code >= 400
          else response.text)
