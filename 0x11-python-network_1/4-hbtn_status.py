#!/usr/bin/python3
""" A module that fetches
    https://alx-intranet.hbtn.io/status
    Using requeats package
"""
import requeats


url = 'https://alx-intranet.hbtn.io/status'
_request = request.get(url)
print("Body response:")
print(f"    - type: {type(_request.text)}")
print(f"    - content: {_request.text}")
