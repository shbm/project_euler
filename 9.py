# PROBLEM 9

# Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
# For example:-
#        3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product a*b*c

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def compute():
    """main: main function"""
    N = 1000
    for i in xrange(1, N+1):
        for j in xrange(i+1, N+1):
            k = N - i - j
            if i**2 + j**2 == k**2:
                if(i + j + k == 1000):
                    return i*j*k

def main():
    import time
    t = time.time()
    print compute()
    print time.time() - t

if __name__ == "__main__":
    main()
