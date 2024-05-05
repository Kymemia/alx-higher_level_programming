#!/usr/bin/python3

"""This script takes one's GitHub credentials(username + Id)
and uses the GitHub API to display the id"""

if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    username, password = sys.argv[1:3]
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {password}"}
    response = requests.get(url, headers=headers)
    print(response.json().get("id"))
