#!/usr/bin/python3
""" A module that replicates Pascal's Triangle in list form """


def pascal_triangle(n):
    """ My function that creates Pascal's Triangle

    Args:
        n: the size if the triangle

    Return:
            a list of lists reping Pascal's Triangle
    """
    lists = []
    if n <= 0:
        return lists
    for size in range(n):
        lst = []
        for idx in range(size + 1):
            if idx == 0 or idx == size:
                val = 1
            else:
                val = lists[size - 1][idx - 1] + lists[size - 1][idx]
            lst.append(val)
        lists.append(lst)
    return lists
