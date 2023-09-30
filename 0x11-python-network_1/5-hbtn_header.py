#!/usr/bin/python3
""" A mkdule that sends a request tona url and displays
    the header with variable X-Request-od
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1]).headers
    print(req.get("X-Request-Id"))
