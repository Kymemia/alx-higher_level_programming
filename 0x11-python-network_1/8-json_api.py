#!/usr/bin/python3

"""This script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user"""

if __name__ == "__main__":
    import sys
    import requests

    url = "http://0.0.0.0:5000/search_user"
    try:
        if len(sys.argv) == 2:
            content = requests.post(url, data={'q': sys.argv[1]})
            jsonData = content.json()
            print(f"[{jsonData.get('id')}] {jsonData.get('name')}"
                  if jsonData else "No result")
        else:
            print("No result")
    except (ValueError, IndexError):
        print("Not a valid JSON")
