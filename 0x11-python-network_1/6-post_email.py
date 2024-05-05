#!/usr/bin/python3

"""This script takes in a URL & an email address,
sends a POST request to the passed URL
with the email as a parameter,
& finally displays the body of the response"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    content = requests.post(url, data=data)
    print(content.text)
