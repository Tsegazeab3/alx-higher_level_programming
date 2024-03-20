#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = sys.argv[2]
    no1 = int(sys.argv[1])
    no2 = int(sys.argv[3])
    operations = {
        "+": calculator_1.add,
        "-": calculator_1.sub,
        "*": calculator_1.mul,
        "/": calculator_1.div,
    }
    if operator in operations:
        result = operations[operator](int(no1), int(no2))
        print("{:d} {:s} {:d} = {:d}".format(no1, operator, no2, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
