#!/usr/bin/python3

"""This script fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
