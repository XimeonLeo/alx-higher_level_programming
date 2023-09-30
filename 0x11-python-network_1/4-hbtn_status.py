#!/usr/bin/python3
""" A module that fetches
    https://alx-intranet.hbtn.io/status
    Using requeats package
"""
import requests


url = 'https://alx-intranet.hbtn.io/status'
_request = requests.get(url)
print("Body response:")
print(f"    - type: {type(_request.text)}")
print(f"    - content: {_request.text}")
