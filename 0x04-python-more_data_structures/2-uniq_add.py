#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = set(my_list)
    _sum = 0
    for element in my_list:
        _sum += element
    return _sum
