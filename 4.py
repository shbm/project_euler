# PROBLEM 4

# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check_palin(number):
    """check_palin: checks if a number is palindrome or not"""
    copy = number
    r = 0
    while copy > 0:
        d = copy % 10
        r = d+r*10
        copy /= 10
    if r == number:
        return True
    else:
        return False

def gen_num():
    """gen_num: generates product of three digit numbers"""
    products = []
    i = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i*j
            if check_palin(product):
                products.append(product)
                i += 1
    products.sort()
    return products[len(products)-1]

def main():
    import time
    t = time.time()
    print gen_num()
    print time.time() - t

if __name__ == "__main__":
    main()
