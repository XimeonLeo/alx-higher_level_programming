#!/usr/bin/python3
""" A module that takes my GitHub credentials and uses
    GitHub API to display my id
    """
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    uname = sys.argv[1]
    passwd = sys.argv[2]

    response = requests.get(url, auth=HTTPBasicAuth(uname, passwd))
    print(response.json().get("id"))
