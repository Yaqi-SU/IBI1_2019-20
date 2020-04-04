# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:03:32 2020

@author: suyaqi
"""

xfile = open('saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
filename=input('Please enter a file name:')

mito={}
mitoseq=''
signal = False
n= 0
for line in xfile:
    line = line.rstrip()
    if not 'R64-1-1:Mito' in line:
        if signal == False:
         continue
        elif '>' in line:
            signal = False
            mito[str(n)]=mitoseq
            mitoseq = ''
            continue
    else:
        signal = True
        n = n+1
    mitoseq=mitoseq+line
import re
temseq=''
noseq=0
genename=''
genelength=0
finalseq=''
for i in range(1,n+1):
    temseq=mito[str(i)]
    genename=re.search(r'gene:(\w+)',temseq)
    genename=genename.group(0)
    for m in range(0,len(temseq)):
        if temseq[m]==']':
            noseq = m+1
    genelength = len(temseq) - noseq
    for h in range(noseq,len(temseq)):
        finalseq=finalseq+temseq[h]
    reverse=finalseq[::-1]
    rev=''
    for a in reverse:
        if a == 'A':
           rev+='T'
        elif a =='T':
           rev+='A'
        elif a =='C':
           rev+='G'
        elif a =='G':
           rev+='C'
    mito[str(i)]= '>Gene:'+ genename+' Length:'+str(genelength)+'bp'+'\n'+rev
    temseq=''
    noseq=0
    genename=''
    genelength=0
    finalseq=''
yfile=open(filename,'w')
for i in range(1,n+1):
    line=mito[str(i)]
    yfile.write(line+'\n')
yfile.close()
zfile=open(filename,'r')
for line in zfile:
    line=line.rstrip()
    print(line)