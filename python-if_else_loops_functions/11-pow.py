#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b < 0:
        b *= -1
        for i in range(1, b + 1):
            result *= a
        return 1 / result
    else:
        for i in range(1, b + 1):
            result *= a
        return result
