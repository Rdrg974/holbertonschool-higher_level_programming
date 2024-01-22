#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        j = ord(str[i])
        if j >= 97 and j <= 122:
            j = ord(str[i]) - 32
        if i == len(str) - 1:
            print("{}".format(chr(j)))
        else:
            print("{}".format(chr(j)), end='')
