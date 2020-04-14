# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:21:25 2020

@author: suyaqi
"""
#Enter a number
k=input('Enter a number:')
t=eval(k)
#Convert the decimal number into binary
a=bin(t)
#Discard 0b
b=a[2:]
#Divide b into a list
c=list(b)
#Loop through all numbers in range(len(c))
n=''
for i in range(len(c)):
    # If c[i]==1: n+=2**(len(c)-i-1)+,i+=1
    c[i]=int(c[i])
    if c[i]==1:
        n+=str(2)+'**'+str(len(c)-i-1)+'+'
        i+=1
        #if not: continue
    else:
        continue
    #When the loop is done, print' k(The number entered) is n[:-1]'
print(eval(k),'is',n[:-1])

   
    
    
  
    
