#!/usr/bin/python3
def no_c(my_string):
    my_2_str = []
    for char in my_string:
        if char != 'c' and char != 'C':
            my_2_str.append(char)
    return ''.join(my_2_str)
