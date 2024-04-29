#!/usr/bin/python3
"""This module  fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {!r}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf-8")))
