#!/usr/bin/python3

"""This script takes in a URL, sends a request to it,
and displays the body of the response(decoded in utf-8)"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse
    import urllib.error

    try:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            content = response.read().decode("utf-8")
            print(content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
