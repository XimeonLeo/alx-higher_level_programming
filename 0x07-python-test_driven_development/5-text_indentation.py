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
    i = 0
    while i < len(text):
        print(f"{text[i]}", end='')
        if text[i] in [".", "?", ":"]:
            print("\n")
            i += 1
        i += 1
