#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


the_url = "https://alx-intranet.hbtn.io/status"


if __name__ == '__main__':
    with urllib.request.urlopen(the_url) as res:
        the_body = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(the_body)))
        print("\t- content: {}".format(the_body))
        print("\t- utf8 content: {}".format(the_body.decode('utf-8')))
