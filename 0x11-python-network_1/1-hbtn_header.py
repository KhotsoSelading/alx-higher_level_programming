#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found
"""
import sys
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            x_request_id = response.headers.get("X-Request-Id")
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id not found in the response headers.")
    except urllib.error.URLError as e:
        print(f"Error: {e}")
