#!/usr/bin/python3
"""
Script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    try:
        data = urllib.parse.urlencode({"email": email})
        data = data.encode()
        request = urllib.request.Request(url, data)
        with urllib.request.urlopen(request) as response:
            response_data = response.read().decode("utf-8")
            print(response_data)

    except urllib.error.URLError as e:
        print(f"Error: {e}")
        sys.exit(1)
