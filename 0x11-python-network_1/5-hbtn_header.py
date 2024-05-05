#!/usr/bin/python3

"""This script takes in a URL, sends a request to the URL,
and displays the value of var, X-Request-Id
in the response header"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    data = requests.get(url)
    xRequestId = data.headers.get('X-Request-Id')
    print(xRequestId)
