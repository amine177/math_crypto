#!/bin/env python3


import sys


def gcd(a: int, b: int) -> int:
    
     
    r = a % b
    a = b
    b = r
    while (r != 0):
        
        r = a % b
        a = b
        b = r
    return a
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: euclid.py a b")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("gcd({}, {}) = {}".format(a, b, gcd(a, b)))
