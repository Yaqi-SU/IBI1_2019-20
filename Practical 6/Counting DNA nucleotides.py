# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:10:14 2020

@author: suyaqi
"""
#Input variables
A=6
G=5
C=4
T=6
#Make the frequency dictionary
gene_dict={'A':A,'G':G,'C':C,'T':T}
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
#Set labels and sizes based on the dictionary
labels = 'A','G','C','T'
sizes = (A,G,C,T)
#Set the colors to be lightgreen, lightskyblue, lightpink ,grey
colors = 'lightgreen','lightskyblue','lightpink','grey'
#Set all gaps to be 0
explode = (0,0,0,0)
#Make the pieplot
plt.pie(sizes, explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=False, startangle=50)
plt.axis('equal')
plt.show()