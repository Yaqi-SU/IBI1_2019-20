# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:10:14 2020

@author: suyaqi
"""
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
#Input a DNA sequence
seq=input('Please enter a DNA sequence:')
#Count the number of AGCT in the input sequence
A=seq.count('A')
C=seq.count('C')
G=seq.count('G')
T=seq.count('T')
#Make the frequency dictionary
gene_dict={'A':A,'G':G,'C':C,'T':T}
print('The frequency dictionary of the input sequence is:',gene_dict)

#Set labels and sizes based on the dictionary
labels = 'A','G','C','T'
sizes = (A,G,C,T)
#Set the colors of the pieplot
colors = 'lightgreen','lightskyblue','lightpink','grey'
#Set all gaps to be 0
explode = (0,0,0,0)
#Make the pieplot
plt.pie(sizes, explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=False, startangle=50)
#Set the shape of the pieplot as circle
plt.axis('equal')
plt.show()