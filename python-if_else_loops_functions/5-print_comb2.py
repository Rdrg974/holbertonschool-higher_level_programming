#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{:02d}".format(i))
    else:
        print("{:02d}, ".format(i), end='')
