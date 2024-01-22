#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    add = cal.add(a, b)
    sub = cal.sub(a, b)
    mul = cal.mul(a, b)
    div = cal.div(a, b)
    print("{} + {} = {}".format(a, b, add))
    print("{} - {} = {}".format(a, b, sub))
    print("{} * {} = {}".format(a, b, mul))
    print("{} / {} = {}".format(a, b, div))
