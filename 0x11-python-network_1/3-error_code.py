#!/usr/bin/python3
""" A module that sends a requeat to a url and displays
    tge body of the response in utf-8
"""
import urllib.request
import sys


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
