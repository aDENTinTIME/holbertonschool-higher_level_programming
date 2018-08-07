#!/usr/bin/python3

import requests
from sys import argv


def main():
    url = argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))

if __name__ == "__main__":
    main()
