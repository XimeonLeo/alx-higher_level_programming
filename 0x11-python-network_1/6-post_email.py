#!/usr/bin/python3
""" A module that Poats an email to a url using
    request module
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    response = requests.post(url, data=value)
    print(response.text)
