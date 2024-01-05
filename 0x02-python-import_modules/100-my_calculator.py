#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    thelen = len(sys.argv) - 1
    if thelen != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    secondop = sys.argv[2]
    if secondop not in ['+', '-', '*', '/']:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if secondop == '+':
            res = add(a, b)
            print(f"{a} {secondop} {b} = {res}")
        elif secondop == '-':
            res = sub(a, b)
            print(f"{a} {secondop} {b} = {res}")
        elif secondop == '*':
            res = mul(a, b)
            print(f"{a} {secondop} {b} = {res}")
        elif secondop == '/':
            res = div(a, b)
            print(f"{a} {secondop} {b} = {res}")
