#!/usr/bin/python3
from calculator_1 import sub as su, add as ad, mul as mu, div as di
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, ad(a, b)))
    print("{} - {} = {}".format(a, b, su(a, b)))
    print("{} * {} = {}".format(a, b, mu(a, b)))
    print("{} / {} = {}".format(a, b, di(a, b)))
