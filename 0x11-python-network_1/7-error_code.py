#!/usr/bin/python3

import requests
from sys import argv


def main():
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print('Error code:', r.status_code)
    else:
        print(r.text)

if __name__ == "__main__":
    main()
