# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:14:47 2020

@author: suyaqi
"""


while True:
    try:
#print 'Enter a positive integer number:'
        print('Enter a positive integer number:')
#if the number input is a positive integer,break while
        n = int(input())
        break
#if not,print 'You gave a noninteger string.'
    except:
        print('You gave a noninteger string.')

# define the collatz function to process n
def collatz(number):
#if the number is even, return number//2
    r = number % 2
    if r == 0:
        return number // 2
#if the number is odd, return 3 * number + 1
    else:
        return 3 * number + 1

# While n !=1： print(collatz(n)).While n=1： done.
while n !=1:
    print(collatz(n))
    n = collatz(n)
