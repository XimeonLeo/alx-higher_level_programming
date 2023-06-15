#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [itr if itr != search else replace for itr in my_list]
    return new_list
