#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_dgt = abs(number) % 10
    else:
        last_dgt = number % 10
    print(f"{last_dgt}", end='')
    return (last_dgt)
