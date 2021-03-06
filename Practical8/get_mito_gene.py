# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:13:07 2020

@author: suyaqi
"""

xfile = open('saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')

mito={}#A dictionary to store the mitochondria sequence
mitoseq=''#An empty string to store a mitochondria sequence temporarily
signal = False# Indication of whether new sequences will be added
n= 0# number of sequences added
for line in xfile:
    line = line.rstrip()
    if not 'R64-1-1:Mito' in line: #If it is not a mitochondria sequence
        if signal == False:
         continue
        elif '>' in line: #Denoting the end of a mitochondira sequence
            signal = False
            mito[str(n)]=mitoseq
            mitoseq = ''#Empty the string to store another mitochondria sequence
            continue
    else:
        signal = True
        n = n+1
    mitoseq=mitoseq+line
import re
temseq=''#An empty string to store an extracted mitochondria sequence from the dictionary temporarily
noseq=0#Denoting the length of the descrition parts of a gene sequence
genename=''
genelength=0
finalseq=''#An empty string to store the final mitochondria sequence
for i in range(1,n+1):
    temseq=mito[str(i)]
    genename=re.search(r'gene:(\w+)',temseq)#Searching the gene name
    genename=genename.group(0)
    for m in range(0,len(temseq)):
        if temseq[m]==']':
            noseq = m+1
    genelength = len(temseq) - noseq
    for h in range(noseq,len(temseq)):
        finalseq=finalseq+temseq[h]
    mito[str(i)]= '>Gene:'+ genename+' Length:'+str(genelength)+'bp'+'\n'+finalseq
    temseq=''#Refresh for the next loop
    noseq=0
    genename=''
    genelength=0
    finalseq=''
yfile=open('Mito_gene.fa','w')#Store the mitochondria sequence in a new file
for i in range(1,n+1):
    line=mito[str(i)]
    yfile.write(line+'\n')
yfile.close()
zfile=open('Mito_gene.fa','r')
for line in zfile:
    line=line.rstrip()
    print(line)
    

    
    
    
    
