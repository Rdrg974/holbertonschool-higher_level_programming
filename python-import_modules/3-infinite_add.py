#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    argument = len(argv) - 1
    if argument > 0:
        for i in range(1, len(argv)):
            result += int(argv[i])
        print("{}".format(result))
    else:
        print("{}".format(result))
