# PROBLEM 20

# n! means n x (n - 1) x ... x 3 x 2 x 1

# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is
#       3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    a = []
    f = 1
    for i in xrange(1, 101):
        f *= i
    print f
    for i in str(f):
        a.append(int(i))
    print "sum", sum(a)

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
