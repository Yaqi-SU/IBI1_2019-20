# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:21:25 2020

@author: suyaqi
"""
#Enter a number
x=input('Enter a number:')
t=eval(x)
#Convert the decimal number into binary
a=bin(t)
#Discard 0b
b=a[2:]
#Divide b into a list
c=list(b)
# Set an empty string to store the powers of 2
n=''
#Loop through all numbers in list b
for i in range(len(c)):
    # If c[i]==1: n=n+2**(len(c)-i-1),i=i+1
    c[i]=int(c[i])
    if c[i]==1:
        n+=str(2)+'**'+str(len(c)-i-1)+'+'
        i+=1
        #if not: continue
    else:
        continue
print(eval(x),'is',n[:-1])

   
    
    
  
    
