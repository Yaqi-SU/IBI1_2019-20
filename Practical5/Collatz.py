# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:14:47 2020

@author: suyaqi
"""



#Define n
n=input('Enter a positive integer number:')
# define the collatz function to process n
def collatz(number):
#if the number is even, return (number//2)
    r = int(number) % 2
    if r == 0:
        return int(number) // 2
#if the number is odd, return (3 * number + 1)
    else:
        return 3 * int(number) + 1

# While n!=1:print(collatz(n)). While n=1：done.
while n !=1:
    print(collatz(n))
    n = collatz(n)
