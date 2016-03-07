# PROBLEM 2
# Each new term in the Fibonacci sequence is generated by adding
# the previous two terms. By starting with 1 and 2, the first 10
# terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values
# do not exceed 4 million, find the sum of the even-valued terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fibonacci():
    """For generating fibonacci numbers"""
    sum = 0
    a = 0
    b = 1
    while a<4000000:
        a, b = b, a+b
        print a
        if a<4000000 and a%2==0:
            sum += a
    print "sum", sum


def fibonacci():
    import time
    t = time.time()
    print gen_num()
    print time.time() - t

if __name__ == "__main__":
    fibonacci()
