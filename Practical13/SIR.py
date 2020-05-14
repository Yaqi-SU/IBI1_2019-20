# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:21:20 2020

@author: suyaqi
"""
#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#Set the parameters
S=9999
I=1
R=0
N=10000
beta=0.3
gamma=0.05
#Set the lists
S1=[]
I1=[]
R1=[]
n=0#Record the loop times
nlist=[]#A list to store loop times
while n <=1000:#loop 1000 times
   infectious=np.random.choice(range(2),S,p=[(I*beta/N),(1-(I*beta/N))])#0 stands for infection and 1 stands for susceptibility, randomly picking 0 and 1 according to the probability
   recover=np.random.choice(range(2),I,p=[gamma,(1-gamma)])#0 stands for recovery and 1 stands for infection, randomly picking 0 and 1 according to the probability
   list0=list(recover)
   rec=list0.count(0)#Count the new recovery cases 
   list1=list(infectious)
   inf=list1.count(0)#Count the new infection cases
   S=S-inf#Susceptibility cases= Original - new infection cases
   I=I+inf-rec#Infection cases=Original + new infection cases - new recovery cases
   R=R+rec#Recovery cases=Original + new recovery cases
   S1.append(S)#Add new S to the S1 list
   I1.append(I)#Add new I to the I1 list
   R1.append(R)#Add new R to the R1 list
   n=n+1#Add the loop time
   nlist.append(n)#Store the loop time in the nlist
#Make the plot
fig,ax=plt.subplots(figsize=(6,4),dpi=150)
ax.plot(nlist,S1,label='Susceptibility')
ax.plot(nlist,R1,label='Recovery')
ax.plot(nlist,I1,label='Infection')
ax.set_xlabel('time')
ax.set_ylabel('number of people')
ax.set_title('SIR model')
ax.legend(loc='upper right')
plt.savefig('C:\\Users\\suyaqi\\Desktop\\IBI1\\IBI1_2019-20\\Practical13\\SIR model',type='png')
plt.show()


   
        
        