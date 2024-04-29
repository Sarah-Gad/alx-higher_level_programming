#!/usr/bin/python3
"""This module sends a POST request to the passed URL"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    processedemail = urllib.parse.urlencode(email).encode("ascii")
    request = urllib.request.Request(url, processedemail)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
