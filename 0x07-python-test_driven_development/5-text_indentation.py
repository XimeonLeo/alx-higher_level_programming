#!/usr/bin/python3
""" Defines a function that looks out for . ? :
    Error:
            TypeError: if a string isnt passed
"""


def text_indentation(text):
    """ The function that prints the text
        Argument:
                text: a string
        Prints a newline whenever a . ? or / is found
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    x = 0
    while x < len(text):
        print(f"{text[x]}", end='')
        if text[x] == '\n' or text[x] in [".", "?", ":"]:
            if text[x] in [".", "?", ":"]:
                print("\n")
            x += 1
            while x < len(text) and text[x] == " ":
                x += 1
            continue
        x += 1
