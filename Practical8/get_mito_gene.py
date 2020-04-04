# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:13:07 2020

@author: suyaqi
"""

xfile = open('saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')

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
    mito[str(i)]= '>Gene:'+ genename+' Length:'+str(genelength)+'bp'+'\n'+finalseq
    temseq=''
    noseq=0
    genename=''
    genelength=0
    finalseq=''
yfile=open('Mito_gene.fa','w')
for i in range(1,n+1):
    line=mito[str(i)]
    yfile.write(line+'\n')
yfile.close()
zfile=open('Mito_gene.fa','r')
for line in zfile:
    line=line.rstrip()
    print(line)
    

    
    
    
    
