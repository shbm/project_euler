# PROBLEM 10

# Find the sum of all the primes below two million.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sieve(n):
    is_prime = [False] * 2 + [True] * (n - 1)
    for i in xrange(int(n**0.5 + 1.5)):
        if is_prime[i]:
            for j in xrange(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def main():
    try:
        primes = sieve(2000000)
        for i in primes:
            i
        lp =  primes[len(primes)-1]
        print len(primes), "  ->  ", lp
        print sum(primes)
    except ValueError:
        print 'Enter only an integer value, n > 1.'
        main()

if __name__ == '__main__':
    main()
