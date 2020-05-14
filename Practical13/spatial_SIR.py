# -*- coding: utf-8 -*-
"""
Created on Wed May 13 09:16:57 2020

@author: suyaqi
"""
#import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#make array of all susceptible population
population=np.zeros((100,100))
#Randomly decide the location of outbreak
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
#plot the initial infected individual
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')
#Set the parameters
beta=0.3
gamma=0.05
n=0
#Loop for 10 times
while n<=10:
# find infected points
   infectedIndex = np.where(population==1)
   recovery=np.where(population==2)
# loop through all infected points

   for i in range(len(infectedIndex[0])):

    # get x, y coordinates for each point

       x = infectedIndex[0][i]

       y = infectedIndex[1][i]

    # infect each neighbour with probability beta

    # infect all 8 neighbours 

       for xNeighbour in range(x-1,x+2):

           for yNeighbour in range(y-1,y+2):

            # avoid infecting yourself

               if (xNeighbour,yNeighbour) != (x,y):

                # avoid falling off an edge

                   if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:

                    # only infect neighbours that are not already infected

                       if population[xNeighbour,yNeighbour]==0:

                           population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])
       #Randomly pick infected individuals to be recovery
       population[x,y]=np.random.choice((1,2),1,p=[1-gamma,gamma])  
   n=n+1
#Reset the parameters for  loops
n1=0 
population1=np.zeros((100,100))
population1[outbreak[0],outbreak[1]]=1
#Loop for 50 times
while n1<=50:
# find infected points

   infectedIndex1 = np.where(population1==1)
   recovery1=np.where(population1==2)
# loop through all infected points

   for i in range(len(infectedIndex1[0])):

    # get x1, y1 coordinates for each point

       x1 = infectedIndex1[0][i]

       y1 = infectedIndex1[1][i]

    # infect each neighbour with probability beta

    # infect all 8 neighbours 

       for xNeighbour1 in range(x1-1,x1+2):

           for yNeighbour1 in range(y1-1,y1+2):

            # avoid infecting yourself

               if (xNeighbour1,yNeighbour1) != (x1,y1):

                # avoid falling off an edge

                   if xNeighbour1 != -1 and yNeighbour1 != -1 and xNeighbour1!=100 and yNeighbour1!=100:

                    # only infect neighbours that are not already infected

                       if population1[xNeighbour1,yNeighbour1]==0:

                           population1[xNeighbour1,yNeighbour1]=np.random.choice(range(2),1,p=[1-beta,beta])
       #Randomly pick infected individuals to be recovery
       population1[x1,y1]=np.random.choice((1,2),1,p=[1-gamma,gamma])  
   n1=n1+1
#Reset the parameters for loops
n2=0
population2=np.zeros((100,100))
population2[outbreak[0],outbreak[1]]=1
#Loop for 100 times
while n2<=100:
# find infected points

   infectedIndex2 = np.where(population2==1)
   recovery2=np.where(population2==2)
# loop through all infected points

   for i in range(len(infectedIndex2[0])):

    # get x2, y2 coordinates for each point

       x2 = infectedIndex2[0][i]

       y2 = infectedIndex2[1][i]

    # infect each neighbour with probability beta

    # infect all 8 neighbours 

       for xNeighbour2 in range(x2-1,x2+2):

           for yNeighbour2 in range(y2-1,y2+2):

            # avoid infecting yourself 

               if (xNeighbour2,yNeighbour2) != (x2,y2):

                # avoid falling off an edge

                   if xNeighbour2 != -1 and yNeighbour2 != -1 and xNeighbour2!=100 and yNeighbour2!=100:

                    # only infect neighbours that are not already infected

                       if population2[xNeighbour2,yNeighbour2]==0:

                           population2[xNeighbour2,yNeighbour2]=np.random.choice(range(2),1,p=[1-beta,beta])
       #Randomly pick infected individuals to be recovery
       population2[x2,y2]=np.random.choice((1,2),1,p=[1-gamma,gamma])  
   n2=n2+1
#Reset the initial population with one infectd individual
population0=np.zeros((100,100))
population0[outbreak[0],outbreak[1]]=1
#Make a series of plots showing the propagation first of the disease and then of resistance against it
fig=plt.figure(figsize=(6,4),dpi=150)
ax0=fig.add_subplot(221)
ax0.imshow(population0,cmap='viridis',interpolation='nearest')
ax1=fig.add_subplot(222)
ax1.imshow(population,cmap='viridis',interpolation='nearest')
ax2=fig.add_subplot(223)
ax2.imshow(population1,cmap='viridis',interpolation='nearest')
ax3=fig.add_subplot(224)
ax3.imshow(population2,cmap='viridis',interpolation='nearest')

