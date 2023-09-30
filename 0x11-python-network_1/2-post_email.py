#!/usr/bin/python3
""" A module that sends a POST requeat to a url of an
    email passed as parameters and displays the body
    of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')  # or utf-8
    _request = urllib.request.Request(url, data)
    with urllib.request.urlopen(_request) as response:
        print(response.read().decode('utf-8'))
