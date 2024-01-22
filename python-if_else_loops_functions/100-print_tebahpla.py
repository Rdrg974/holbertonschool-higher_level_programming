#!/usr/bin/python3
char = 'z'
i = ord(char)
while i >= 97:
    char = chr(i)
    if i % 2 == 1:
        char = chr(i - 32)
    print("{}".format(char), end='')
    i = i - 1
