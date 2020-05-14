# -*- coding: utf-8 -*-
"""
Created on Wed May 13 07:54:49 2020

@author: suyaqi
"""
#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#Set the parameters
I=1
R=0
N=10000
S=9999
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
   #R=R+rec#Recovery cases=Original + new recovery cases
   #S1.append(S)#Add new S to the S1 list
   I1.append(I)#Add new I to the I1 list
   #R1.append(R)#Add new R to the R1 list
   n=n+1#Add the loop time
   nlist.append(n)#Store the loop time in the nlist
V1=int((1/10)*9999)
S2=9999-V1
I2list=[]
n1=0
I2=1


while n1 <=1000:#loop 1000 times
   infectious1=np.random.choice(range(2),S2,p=[(I2*beta/N),(1-(I2*beta/N))])#0 stands for infection and 1 stands for susceptibility, randomly picking 0 and 1 according to the probability
   recover1=np.random.choice(range(2),I2,p=[gamma,(1-gamma)])#0 stands for recovery and 1 stands for infection, randomly picking 0 and 1 according to the probability
   list2=list(recover1)
   rec1=list2.count(0)#Count the new recovery cases 
   list3=list(infectious1)
   inf1=list3.count(0)#Count the new infection cases
   S2=S2-inf1#Susceptibility cases= Original - new infection cases
   I2=I2+inf1-rec1#Infection cases=Original + new infection cases - new recovery cases
   I2list.append(I2)
   n1=n1+1#Add the loop time
   
V2=int((2/10)*9999)
S3=9999-V2
I3list=[]
n2=0
I3=1
while n2 <=1000:#loop 1000 times
   infectious2=np.random.choice(range(2),S3,p=[(I3*beta/N),(1-(I3*beta/N))])#0 stands for infection and 1 stands for susceptibility, randomly picking 0 and 1 according to the probability
   recover2=np.random.choice(range(2),I3,p=[gamma,(1-gamma)])#0 stands for recovery and 1 stands for infection, randomly picking 0 and 1 according to the probability
   list4=list(recover2)
   rec2=list4.count(0)#Count the new recovery cases 
   list5=list(infectious2)
   inf2=list5.count(0)#Count the new infection cases
   S3=S3-inf2#Susceptibility cases= Original - new infection cases
   I3=I3+inf2-rec2#Infection cases=Original + new infection cases - new recovery cases
   I3list.append(I3)
   n2=n2+1#Add the loop time
V3=int((3/10)*9999)
S4=9999-V3
I4list=[]
n3=0
I4=1
while n3 <=1000:#loop 1000 times
   infectious3=np.random.choice(range(2),S4,p=[(I4*beta/N),(1-(I4*beta/N))])#0 stands for infection and 1 stands for susceptibility, randomly picking 0 and 1 according to the probability
   recover3=np.random.choice(range(2),I4,p=[gamma,(1-gamma)])#0 stands for recovery and 1 stands for infection, randomly picking 0 and 1 according to the probability
   list6=list(recover3)
   rec3=list6.count(0)#Count the new recovery cases 
   list7=list(infectious3)
   inf3=list7.count(0)#Count the new infection cases
   S4=S4-inf3#Susceptibility cases= Original - new infection cases
   I4=I4+inf3-rec3#Infection cases=Original + new infection cases - new recovery cases
   I4list.append(I4)
   n3=n3+1#Add the loop time
V4=int(0.4*9999)
S5=9999-V4
I5list=[]
n4=0
I5=1
while n4 <=1000:#loop 1000 times
   infectious4=np.random.choice(range(2),S5,p=[(I5*beta/N),(1-(I5*beta/N))])#0 stands for infection and 1 stands for susceptibility, randomly picking 0 and 1 according to the probability
   recover4=np.random.choice(range(2),I5,p=[gamma,(1-gamma)])#0 stands for recovery and 1 stands for infection, randomly picking 0 and 1 according to the probability
   list8=list(recover4)
   rec4=list8.count(0)#Count the new recovery cases 
   list9=list(infectious4)
   inf4=list9.count(0)#Count the new infection cases
   S5=S5-inf4#Susceptibility cases= Original - new infection cases
   I5=I5+inf4-rec4#Infection cases=Original + new infection cases - new recovery cases
   I5list.append(I5)
   n4=n4+1#Add the loop time
V5=int(0.5*9999)
S6=9999-V5
I6list=[]
n5=0
I6=1
while n5 <=1000:#loop 1000 times
   infectious5=np.random.choice(range(2),S6,p=[(I6*beta/N),(1-(I6*beta/N))])#0 stands for infection and 1 stands for susceptibility, randomly picking 0 and 1 according to the probability
   recover5=np.random.choice(range(2),I6,p=[gamma,(1-gamma)])#0 stands for recovery and 1 stands for infection, randomly picking 0 and 1 according to the probability
   list10=list(recover5)
   rec5=list10.count(0)#Count the new recovery cases 
   list11=list(infectious5)
   inf5=list11.count(0)#Count the new infection cases
   S6=S6-inf5#Susceptibility cases= Original - new infection cases
   I6=I6+inf5-rec5#Infection cases=Original + new infection cases - new recovery cases
   I6list.append(I6)
   n5=n5+1#Add the loop time
V6=int(0.6*9999)
S7=9999-V6
I7list=[]
n6=0
I7=1
while n6 <=1000:#loop 1000 times
   infectious6=np.random.choice(range(2),S7,p=[(I7*beta/N),(1-(I7*beta/N))])#0 stands for infection and 1 stands for susceptibility, randomly picking 0 and 1 according to the probability
   recover6=np.random.choice(range(2),I7,p=[gamma,(1-gamma)])#0 stands for recovery and 1 stands for infection, randomly picking 0 and 1 according to the probability
   list12=list(recover6)
   rec6=list12.count(0)#Count the new recovery cases 
   list13=list(infectious6)
   inf6=list13.count(0)#Count the new infection cases
   S7=S7-inf6#Susceptibility cases= Original - new infection cases
   I7=I7+inf6-rec6#Infection cases=Original + new infection cases - new recovery cases
   I7list.append(I7)
   n6=n6+1#Add the loop time
V7=int(0.7*9999)
S8=9999-V7
I8list=[]
n7=0
I8=1
while n7 <=1000:#loop 1000 times
   infectious7=np.random.choice(range(2),S8,p=[(I8*beta/N),(1-(I8*beta/N))])#0 stands for infection and 1 stands for susceptibility, randomly picking 0 and 1 according to the probability
   recover7=np.random.choice(range(2),I8,p=[gamma,(1-gamma)])#0 stands for recovery and 1 stands for infection, randomly picking 0 and 1 according to the probability
   list14=list(recover7)
   rec7=list14.count(0)#Count the new recovery cases 
   list15=list(infectious7)
   inf7=list15.count(0)#Count the new infection cases
   S8=S8-inf7#Susceptibility cases= Original - new infection cases
   I8=I8+inf7-rec7#Infection cases=Original + new infection cases - new recovery cases
   I8list.append(I8)
   n7=n7+1#Add the loop time
V8=int(0.8*9999)
S9=9999-V8
I9list=[]
n8=0
I9=1
while n8 <=1000:#loop 1000 times
   infectious8=np.random.choice(range(2),S9,p=[(I9*beta/N),(1-(I9*beta/N))])#0 stands for infection and 1 stands for susceptibility, randomly picking 0 and 1 according to the probability
   recover8=np.random.choice(range(2),I9,p=[gamma,(1-gamma)])#0 stands for recovery and 1 stands for infection, randomly picking 0 and 1 according to the probability
   list16=list(recover8)
   rec8=list16.count(0)#Count the new recovery cases 
   list17=list(infectious8)
   inf8=list17.count(0)#Count the new infection cases
   S9=S9-inf8#Susceptibility cases= Original - new infection cases
   I9=I9+inf8-rec8#Infection cases=Original + new infection cases - new recovery cases
   I9list.append(I9)
   n8=n8+1#Add the loop time
V9=int(0.9*9999)
S10=9999-V9
I10list=[]
n9=0
I10=1
while n9 <=1000:#loop 1000 times
   infectious9=np.random.choice(range(2),S10,p=[(I10*beta/N),(1-(I10*beta/N))])#0 stands for infection and 1 stands for susceptibility, randomly picking 0 and 1 according to the probability
   recover9=np.random.choice(range(2),I10,p=[gamma,(1-gamma)])#0 stands for recovery and 1 stands for infection, randomly picking 0 and 1 according to the probability
   list18=list(recover9)
   rec9=list18.count(0)#Count the new recovery cases 
   list19=list(infectious9)
   inf9=list19.count(0)#Count the new infection cases
   S10=S10-inf9#Susceptibility cases= Original - new infection cases
   I10=I10+inf9-rec9#Infection cases=Original + new infection cases - new recovery cases
   I10list.append(I10)
   n9=n9+1#Add the loop time
V10=int(1*9999)
S11=9999-V10
I11list=[]
n10=0
I11=1
while n10 <=1000:#loop 1000 times
   infectious10=np.random.choice(range(2),S11,p=[(I11*beta/N),(1-(I11*beta/N))])#0 stands for infection and 1 stands for susceptibility, randomly picking 0 and 1 according to the probability
   recover10=np.random.choice(range(2),I11,p=[gamma,(1-gamma)])#0 stands for recovery and 1 stands for infection, randomly picking 0 and 1 according to the probability
   list20=list(recover10)
   rec10=list20.count(0)#Count the new recovery cases 
   list21=list(infectious10)
   inf10=list21.count(0)#Count the new infection cases
   S11=S11-inf10#Susceptibility cases= Original - new infection cases
   I11=I11+inf10-rec10#Infection cases=Original + new infection cases - new recovery cases
   I11list.append(I11)
   n10=n10+1#Add the loop time

#Make the plot
fig,ax=plt.subplots(figsize=(6,4),dpi=150)
ax.plot(nlist,I1,label='0')
ax.plot(nlist,I2list,label='10%')
ax.plot(nlist,I3list,label='20%')
ax.plot(nlist,I4list,label='30%')
ax.plot(nlist,I5list,label='40%')
ax.plot(nlist,I6list,label='50%')
ax.plot(nlist,I7list,label='60%')
ax.plot(nlist,I8list,label='70%')
ax.plot(nlist,I9list,label='80%')
ax.plot(nlist,I10list,label='90%')
ax.plot(nlist,I11list,label='100%')
ax.set_xlabel('time')
ax.set_ylabel('number of people')
ax.set_title('SIR model with different vaccination rates')
ax.legend(loc='upper right')
plt.savefig('C:\\Users\\suyaqi\\Desktop\\IBI1\\IBI1_2019-20\\Practical13\\SIR_vaccination',type='png')
plt.show()

   
















