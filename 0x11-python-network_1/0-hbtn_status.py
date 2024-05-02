#!/usr/bin/python3
"""This is a script that fetches a URL"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

#sends a get request to the URL, reads the response body, and decodes it
with urllib.request.urlopen(url) as response:
    body = response.read()

print("\t- Body response:")
print("\t\t- type:", type(body))
print("\t\t- content:", body)
print("\t\t- utf8 content:", body.decode('utf-8'))
