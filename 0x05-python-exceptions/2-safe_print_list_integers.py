#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    itr = 0
    for idx in range(0, x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            itr = itr + 1
        except (TypeError, ValueError):
            continue
    print()
    return itr
