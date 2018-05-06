#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new = text.split(".")
    new = [x.strip(" ") for x in new]
    new = '.\n\n'.join(new)

    new = new.split("?")
    new = [x.strip(" ") for x in new]
    new = '?\n\n'.join(new)

    new = new.split(":")
    new = [x.strip(" ") for x in new]
    new = ':\n\n'.join(new)

    print(new, end="")
