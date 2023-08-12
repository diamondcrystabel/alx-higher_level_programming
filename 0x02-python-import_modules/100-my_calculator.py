#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    argc = len(argv[1:])

    if argc != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        op = str(argv[2])
        a = int(argv[1])
        b = int(argv[3])

        if op not in ["+", "-", "*", "/"]:
            print(f"Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if op == "+":
                res = add(a, b)
            if op == "-":
                res = sub(a, b)
            if op == "*":
                res = mul(a, b)
            if op == "/":
                res = div(a, b)
            print("{0} {1} {2} = {3}".format(a, op, b, res))
