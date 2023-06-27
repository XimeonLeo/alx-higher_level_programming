#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    itr = 0
    for elem in my_list:
        if itr < x:
            try:
                print(f"{elem}", end='')
                itr = itr + 1
            except IndexError:
                break
    print()
    return itr
