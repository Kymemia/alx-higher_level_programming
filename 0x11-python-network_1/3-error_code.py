#!/usr/bin/python3

"""This script takes in a URL, sends a request to it,
and displays the body of the response(decoded in utf-8)"""

if __name__ == "__main__":
    import sys
    import requests

    try:
        url = sys.argv[1]
        response = requests.get(url)
        content = response.text
        print(content)
    except requests.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
