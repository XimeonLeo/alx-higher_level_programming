#!/usr/bin/python3
for num in range(0, 8):
    for ber in range(num + 1, 10):
        print("{}{}, ".format(num, ber), end='')
print("{}".format(89))
