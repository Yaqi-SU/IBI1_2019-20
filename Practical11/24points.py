# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:51:07 2020

@author: suyaqi
"""
#Import necessary libraries
import itertools
import fractions
import sys
x=input('''Please input numbers to compute 24 (use ',' to devide them): ''') 
num=x.split(',')
num_int = [int(x) for x in num]
num_int.sort() 
N=len(num_int)
def calculate1(a,b): #define the function for doing all possible calculations (note that a number cannot be divided by 0)
    if a!=0 and b!=0:
        c=[a+b,b-a,a*b,fractions.Fraction(a,b),fractions.Fraction(b,a)] # The outcome of fractions.Fraction(a,b) is a/b
    if a==0 and b!=0:
        c=[a+b,b-a,a*b,fractions.Fraction(a,b)]
    if a!=0 and b==0:
        c=[a+b,b-a,a*b,fractions.Fraction(b,a)]
    if a==0 and b==0:
        c=[a+b,b-a,a*b]
    return c
def calculate2(i):#define the function for performing calculations among the input numbers
    seq = list(sequence[i]) 
    m = calculate1(seq[0],seq[1])
    del seq[0:2] # Delete the two numbers used in the calculate1()
    while seq!=[]: # Repeat until every number in 'seq' is deleted 
        m_copy = m 
        m=[]
        for j in m_copy:
            m += calculate1(j,seq[0]) 
        del seq[0] 
    return m
for i in range(0, N):
    if (int(num_int[i])<1 or int(num_int[i])>23) : #Check whether the input numbers are 1~23.
        print('The input number must be integers from 1 to 23!')
        sys.exit()    
list1_time = 0
recursion_time = 0
for i in range(N, 1, -1):        
    sequence = list(itertools.permutations(num_int, i)) #Permutation of input numbers
    list1 = []
    for i in range(0, len(sequence)): #perform calculate2() on every possible order of input numbers
        list1 += calculate2(i)
        list1_time = len(list1) # The recursion time of this for-loop 
        if 24 in list1: # When  24 is found, exit the program and output the whole recursion time.
            print('\nYes')
            print('recursion times: '+ str(recursion_time + list1_time) + '\n') # The whole recursion time = recursion time of the last for-loop + list1_time
            sys.exit()
        recursion_time += len(list1) # Record the whole recursion time 
print('No\nReursion time:',recursion_time) #If 24 is not found, print the outcome of recursion time