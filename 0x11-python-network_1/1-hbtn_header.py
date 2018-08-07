#!/usr/bin/python3

import urllib.request
from sys import argv


def main():
    with urllib.request.urlopen(argv[1]) as response:
        html = response.info()
        html_dict = dict(html)
        print(html_dict.get('X-Request-Id'))

if __name__ == "__main__":
    main()
