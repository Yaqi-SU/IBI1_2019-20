# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:31:33 2020

@author: suyaqi
"""
import pandas as pd
human=open('SOD2_human.fa','r')
mouse=open('SOD2_mouse.fa','r')
random=open('RandomSeq.fa','r')
matrix=pd.read_csv('matrix.csv')
seq1=''
seq2=''
seq3=''
score=0
score1=0
score2=0
for line in human:
    if not 'human' in line:
        seq1 = seq1 + line
for line in mouse:
    if not 'mouse' in line:
        seq2=seq2+line
data1=matrix.iloc[:,0]
data2=matrix.iloc[3,:]
alignment=''
alignment1=''
alignment2=''
for i in range(len(seq1)):
    for j in range(0,27):
        for m in range(0,24):
            if seq1[i]==data1[j] and seq2[i]==data2[m] and seq1[i]==seq2[i]:
                score=score+int(matrix.iloc[j,m])
                alignment=alignment+seq1[i]
            elif seq1[i]==data1[j] and seq2[i]==data2[m] and seq1[i]!=seq2[i]:
                 score=score+int(matrix.iloc[j,m])
                 if int(matrix.iloc[j,m]) > 0:
                     alignment = alignment + '+'
                 else:
                     alignment = alignment + ''
                 continue
print('The sum scores between human and mouse is',score)
print(seq1,alignment)
for line in random:
    if not 'Random' in line:
        seq3=seq3+line
for k in range(len(seq1)):
    for n in range(0,27):
        for l in range(0,24):
            if seq1[k]==data1[n] and seq3[k] ==data2[l] and seq1[k]==seq3[k]:
                score1 = score1+int(matrix.iloc[n,l])
                alignment1=alignment1+seq1[k]
            elif seq1[k]==data1[n] and seq3[k] ==data2[l] and seq1[k]!=seq3[k]:
                 score1 = score1+int(matrix.iloc[n,l])
                 if int(matrix.iloc[n,l]) > 0:
                      alignment1 = alignment1 + '+'
                 else:
                     alignment1 = alignment1 + ''
                 continue
print('The sum scores between human and random is',score1)
print(seq1,alignment1)
for x in range(len(seq2)):
    for y in range(0,27):
        for z in range(0,24):
            if seq2[x]==data1[y] and seq3[x] ==data2[z] and seq2[x]==seq3[x]:
                score2 = score2+int(matrix.iloc[y,z])
                alignment2=alignment2+seq2[x]
            elif seq2[x]==data1[y] and seq3[x] ==data2[z] and seq2[x]!=seq3[x]:
                score2 = score2+int(matrix.iloc[y,z])
                if int(matrix.iloc[y,z])>0:
                    alignment2=alignment2+'+'
                else:
                    alignment2=alignment2+''
                continue
print('The sum scores between mouse and random is',score2)
print(seq2,alignment2)
#Calculate the percentage identity
Haming_distance1 =0
Haming_distance2=0
Haming_distance3=0
for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        Haming_distance1 +=1
for j in range(len(seq2)):
    if seq1[j] != seq3[j]:
        Haming_distance2+=1
    else:
       continue
for k in range(len(seq3)):
    if seq3[k]!=seq2[k]:
        Haming_distance3+=1
    else:
        continue
ID1 = (len(seq1)-Haming_distance1)/len(seq1)*100
ID2 = (len(seq2)-Haming_distance2)/len(seq2)*100 
ID3 = (len(seq3)-Haming_distance3)/len(seq3)*100
print('The hamming distance between human and mouse is',Haming_distance1)
print('The hamming distance between human and random is',Haming_distance2)
print('The hamming distance between mouse and random is',Haming_distance3)
print('The percentage identity between human and mouse is',ID1,'%')
print('The percentage identity between human and random is', ID2,'%')
print('The percentage identity between mouse and random is', ID3,'%')
                
            
            
    