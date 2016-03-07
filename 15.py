# PROBLEM 15

# Starting in the top left corner of a 2x2 grid, and only being able
# to move to the right and down, there are exactly 6 routes to the
# bottom right corner.

# How many such routes are there through a 20x20 grid?

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def combination(a, b):
    """combination: Return aCb and a>b"""
    num = math.factorial(a)
    den = math.factorial(b)*(math.factorial(a-b))
    return num/den

def main():
    import time
    t = time.time()
    print combination(40, 20)
    print time.time() - t

if __name__ == '__main__':
    main()
