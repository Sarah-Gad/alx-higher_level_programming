#!/usr/bin/python3
"""This script sends a POST request to the passed URL """

import sys
import requests

if __name__ == "__main__":
    thedata = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data=thedata)
    print(r.text)
