#!/usr/bin/python3
import hidden_4


def main():
    for rect in dir(hidden_4):
        if not rect[:2] == "__":
            print(rect)
if __name__ == "__main__":
    main()
