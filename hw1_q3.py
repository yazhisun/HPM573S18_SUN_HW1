# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:22:00 2018

@author: Administrator
"""

#. Write an iterative function and a recursive
#function that computes the sum of all numbers from 1 to n, where n is given as parameter. Test both
#functions for n = 100

#iterative function
def sumiter(n):
    sum=0
    for i in range(1, n+1):
        sum +=i
    return sum

print(sumiter(100))
#recursion function
def sumrec(n):
    if n==1:
        return 1
    else:
        return n+sumrec(n-1)

print(sumrec(100))