# PROBLEM 17

# If the numbers 1 to 5 are written out in words: one, two, three,
# four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used
# in total. If all the numbers from 1 to 1000 (one thousand) inclusive
# were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example,
# 342(three hundred and forty-two) contains23 letters and 115
# (one hundred and fifteen) contains 20 letters.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

ones = ["","one ","two ","three ","four ","five ","six ","seven ","eight ","nine "]
tens = ["","ten ","twenty ","thirty ","forty ","fifty ","sixty ","seventy ","eighty ","ninety "]
teens = ["","eleven ","twelve ","thirteen ","fourteen ","fifteen ","sixteen ","seventeen ","sixteen ","seventeen ","eighteen ","nineteen "]
hundreds = ["hundred "]
thousands = ["thousand "]

def numToArray(num):
    numArray = [0,0,0,0]
    numArray[0] = num/1000%10       #Thousands place
    numArray[1] = num/100%10        #Hundreds place
    numArray[2] = num/10%10         #Tens place
    numArray[3] = num/1%10          #Ones place
    return numArray

y = []
x = numToArray(1234)
for i in x:
    if i != 0:
        break
    else:
        y.append(i)
del x[0:len(y)]
print x

lenth = len(x)
print lenth

word = ""

if lenth == 4:
    word += ones[x[0]]
    word += thousands[0]
    if x[1] != 0:
        word += ones[x[1]]
        word += hundreds[0]


print word
