#!/usr/bin/python3
"""THis script takes in a URL, sends a request to it,
and displays the value of variable, X-Request-Id,
found in the header of the response"""
from urllib.request import Request, urlopen
from sys import argv

if __name__=="__main__":
    req = Request(argv[1])

    with urlopen(req) as res:
        headers = res.info()
        print(headers.get('X-Request-Id'))
