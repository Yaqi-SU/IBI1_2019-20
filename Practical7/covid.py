# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:47:52 2020

@author: suyaqi
"""
#Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 1.Import the .csv file
os.chdir('C:\\Users\\suyaqi\\Desktop\\IBI1\\IBI1_2019-20\\Practical7')
covid_data=pd.read_csv('full_data.csv')
# 2.Show all rows, and every third column between(and including) 0 and 15
covid_data.iloc[0:16,0:6:3]
# 3.Show "total cases" for all rows corresponding to Afghanistan
data1=covid_data.iloc[:,1]
Boolean_list=[]#Create an empty list to store boolean variables
for i in range(0,7996):
    if data1[i]=='Afghanistan':
        Boolean_list.append(True)
    else:
        Boolean_list.append(False)
totalcases=[False,False,False,False,True,False]
Afghanistan_totalcases=covid_data.iloc[Boolean_list,totalcases]
print(Afghanistan_totalcases)
#4.Compute the mean and median of new cases for the entire world
list1=[]#An empty list to store the rows of World cases
for m in range(0,7996):
    if data1[m]=='World':
        list1.append(m)
    else:
        continue
world_dates=covid_data.loc[list1,'date']
world_newcases=covid_data.loc[list1,'new_cases']
median_newcases=np.median(world_newcases)
mean_newcases=np.mean(world_newcases)
print('The mean for new cases around the world is',mean_newcases)
print('The median for new cases around the world is',median_newcases)
#5.Create a boxplot of new cases worldwide
plt.boxplot(world_newcases,vert=True,whis=1.5,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=False)
plt.title('World new cases')
plt.ylabel('Number')
plt.show()
#6.PLot both new cases and new deaths worldwide
plt.plot(world_dates,world_newcases,'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)#Adjustments to x labels
plt.title('World new cases')
plt.ylabel('Number of new cases')
plt.show()
world_newdeaths=covid_data.loc[list1,'new_deaths']
plt.plot(world_dates,world_newdeaths,'r+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('World new deaths')
plt.ylabel('Number of new deaths')
plt.show()
#7.Answering the question:Are there places in the World there have not yet been more than 10 total infections(as on 31 March)? If so, where are they?
list4=[]#An empty list to store rows of World cases on '2020-03-31
for q in range(0,7996):
    if data1[q] !='World' and covid_data.loc[q,'date']=='2020-03-31':
        list4.append(q)
    else:
        continue
country_total=covid_data.loc[list4,'total_cases']
list5=[]#An empty list to store rows of places with less than 10 cases
list6=[10]
for j in list4:
    if country_total[j] <=list6:
        list5.append(j)
    else:
        continue
places=covid_data.loc[list5,'location']
answer=''#An empty string to store the names of places with less than 10 cases
if len(list5)==0:
    print('No, there are not places in the world where there have not yet been more than 10 total infections.')
else:
    for k in list5:
        if k ==list5[len(list5)-1]:
            answer = answer+places[k]+'.'
        else:
            answer = answer+places[k]+','
    print('Yes. They are',answer)
 
    
        


