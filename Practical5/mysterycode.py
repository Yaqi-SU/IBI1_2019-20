# What does this piece of code do?
# Answer: This code is to randomly find a prime number between 1 and 100. 

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
    n = randint(1,100) #n is drawn randomly between 1 and 100.
    u = ceil(n**(0.5)) #u is the ceiling of n**(0.5)
    for i in range(2,u+1): #i consists of all integers between 2 and u+1 including 2 but without u+1
        if n%i == 0: #if n is divisible by i, the loop will continue.
            p=False


     
print(n) 
