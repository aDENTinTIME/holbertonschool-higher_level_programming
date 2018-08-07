#!/usr/bin/python3

import urllib.request
import urllib.parse
import urllib.error
from sys import argv


def main():
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as page:
            print(page.read().decode())
    except urllib.error.URLError as e:
        print('Error code:', e.status)

if __name__ == "__main__":
    main()
