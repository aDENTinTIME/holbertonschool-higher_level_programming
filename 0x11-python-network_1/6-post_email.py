#!/usr/bin/python3

import requests
from sys import argv


def main():
    url = argv[1]
    values = {'email': argv[2]}
    r = requests.post(url, data=values)
    print(r.text)

if __name__ == "__main__":
    main()
