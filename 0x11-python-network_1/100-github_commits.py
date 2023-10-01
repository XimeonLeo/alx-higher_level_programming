#!/usr/bin/python3
"""A module that prints out the 10 latest commits from github"""
import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[1]
    name = sys.argv[2]
    url = f'http://api.github.com/repos/{repo}/{name}/commits'
    response = requests.get(url)

    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get("sha")
        pusher = commit["commit"]["author"]["name"]

        print(f'{sha}: {pusher}')
