#!/usr/bin/python3

"""This script lists 10 commits(from oldest-newest)
of the repository "rails" by the user "rails"
One must use the GitHub API and print all commits by:
    `<sha>: <author name>` (one by line)
Script takes 2 args:
    arg_1 = repository name
    arg_2 = owner name
Must use requests and sys packages only"""

if __name__ == "__main__":
    import requests
    import sys

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        jsonData = response.json()

        if isinstance(jsonData, list):
            for i, data in enumerate(jsonData[:10]):
                print(f"{data['sha']}: {data['commit']['author']['name']}")
        else:
            print("invalid JSON data")
    else:
        print(f"status code: {response.status_code}")
