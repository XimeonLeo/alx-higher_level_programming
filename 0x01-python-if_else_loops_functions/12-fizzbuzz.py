#!/usr/bin/python3
def fizzbuzz():
    for dgt in range(1, 101):
        if dgt % 3 == 0 and dgt % 5 == 0:
            print(f"FizzBuzz ", end='')
        elif dgt % 3 == 0:
            print(f"Fizz ", end='')
        elif dgt % 5 == 0:
            print(f"Buzz ", end='')
        else:
            print(f"{dgt} ", end='')
