#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and
displays the body of the response (decoded in utf-8).
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with request.urlopen(url) as res:
            body = res.read().decode('utf-8')
            print(body)
    except error.HTTPError as er:
        print(f'Error code: {er.code}')
