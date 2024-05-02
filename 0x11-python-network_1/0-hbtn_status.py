#!/usr/bin/python3
"""This is a script that fetches a URL"""

if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"

    """sends a get request to the URL,
    reads the response body, and decodes it"""
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("\t- Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf8')}")
