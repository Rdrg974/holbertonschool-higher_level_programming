#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cal
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        if op not in {'+', '-', '*', '/'}:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if op == '+':
                print("{} {} {} = {}".format(a, op, b, cal.add(a, b)))
            elif op == '-':
                print("{} {} {} = {}".format(a, op, b, cal.sub(a, b)))
            elif op == '*':
                print("{} {} {} = {}".format(a, op, b, cal.mul(a, b)))
            elif op == '/':
                print("{} {} {} = {}".format(a, op, b, cal.div(a, b)))
            sys.exit(0)
