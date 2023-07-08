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
        if text[x] in [".", "?", ":"]:
            print("\n")
            y = x + 1
            while text[y] == " ":
                x += 1
                y += 1
        x += 1
