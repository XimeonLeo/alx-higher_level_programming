#!/usr/bin/python3
"""A module that prints out the 10 latest commits from github"""
import sys
import requests


if __name__ == '__main__':
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    response = requests.get(url)

    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get("sha")
        pusher = commit["commit"]["author"]["name"]

        print(f'{sha}: {pusher}')
