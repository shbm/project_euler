# Problem 34

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math

cache = {}

def fact(x):
    return cache.setdefault(x,math.factorial(x))

def if_curious(n):
    sum = 0
    for i in str(n):
        if sum > n:
            return False
        sum += fact(int(i))
    if sum == n:
        return True
    return False

def main():
    s = 0
    for i in xrange(10, fact(9)+1):
        if if_curious(i):
            s = s+i
    print s

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
