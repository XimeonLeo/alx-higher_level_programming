#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lent_a = len(tuple_a)
    lent_b = len(tuple_b)
    if lent_a == 0:
        a1 = 0
        b1 = 0
    elif lent_a < 2 and lent_a != 0:
        a1 = tuple_a[0]
        b1 = 0
    else:
        a1 = tuple_a[0]
        b1 = tuple_a[1]
    if lent_b == 0:
        a2 = 0
        b2 = 0
    elif lent_b < 2 and lent_b != 0:
        a2 = tuple_b[0]
        b2 = 0
    else:
        a2 = tuple_b[0]
        b2 = tuple_b[1]
    new_tuple = (a1 + a2, b1 + b2)
    return new_tuple
