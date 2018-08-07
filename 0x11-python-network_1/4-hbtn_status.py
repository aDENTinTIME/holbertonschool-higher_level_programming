#!/usr/bin/python3

import requests


def main():
    r = requests.get('https://intranet.hbtn.io/status')
    r = r.text
    print('Body response:')
    print('\t- type:', type(r))
    print('\t- content:', r)

if __name__ == "__main__":
    main()
