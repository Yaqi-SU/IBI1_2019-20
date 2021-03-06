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
seq1=''#An empty string to store the SOD2_human sequence
seq2=''#An empty string to store the SOD2_mouse sequence
seq3=''#An emoty string to store the Random sequence
score=0#The BLOSUM scores of human_mouse
score1=0#The BLOSUM scores of human_random
score2=0#The BLOSUM scores of mouse_random
for line in human:
    if not 'human' in line:
        seq1 = seq1 + line
for line in mouse:
    if not 'mouse' in line:
        seq2=seq2+line
data1=matrix.iloc[:,0]#All rows of amino acids in the matrix
data2=matrix.iloc[3,:]#All columns of amino acids in the matrix
alignment=''#An empty string to store the alignment of human_mouse
alignment1=''#An empty string to store the alignment of human_random
alignment2=''#An empty string to store the alignment of mouse_random
for i in range(len(seq1)):#loop through human sequence
    for j in range(0,27):#loop through the rows of amino acids
        for m in range(0,24):#loop through the columns of amino acids
            if seq1[i]==data1[j] and seq2[i]==data2[m] and seq1[i]==seq2[i]:#If the amino acids in two sequence are the same
                score=score+int(matrix.iloc[j,m])
                alignment=alignment+seq1[i]#Add the amino acid in the alignment
            elif seq1[i]==data1[j] and seq2[i]==data2[m] and seq1[i]!=seq2[i]:# If the amino acids in two sequence are not the same
                 score=score+int(matrix.iloc[j,m])
                 if int(matrix.iloc[j,m]) > 0:#If the BLOSUM score is positive
                     alignment = alignment + '+'#Add "+" to the alignment
                 else:#If the BLOSUM score is negative
                     alignment = alignment + '-'#Add "-" to the alingment
                 continue
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
                     alignment1 = alignment1 + '-'
                 continue

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
                    alignment2=alignment2+'-'
                continue
            
            
#Calculate the hamming distance 
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
    
#Calculate the percentage identity
ID1 = (len(seq1)-Haming_distance1)/len(seq1)*100
ID2 = (len(seq2)-Haming_distance2)/len(seq2)*100 
ID3 = (len(seq3)-Haming_distance3)/len(seq3)*100


#Print out the outcomes
print ('A comparsion between SOD2_human and SOD2_mouse\nSOD2_human:\n',seq1, '\nAlignment:\n', alignment, '\n\nSOD_mouse:\n',seq2, '\nThe final BLOSUM score is', str(score),'.','\nThe Hamming distance is', str(Haming_distance1), ', the percentage identity of them is', ID1, '%.\n\n' )
print ('A comparsion between SOD2_human and RandomSeq\nSOD2_human:\n',seq1, '\nAlignment:\n', alignment1, '\n\nRandomSeq:\n',seq3, '\nThe final BLOSUM score is', str(score1),'.','\nThe Hamming distance is', str(Haming_distance2), ', the percentage identity  of them is', ID2, '%.\n\n' )
print ('A comparsion between RandomSeq and SOD2_mouse\nRandomSeq:\n',seq3, '\nAlignment:\n', alignment2, '\n\nSOD_mouse:\n',seq2, '\nThe final BLOSUM score is', str(score2),'.','\nThe Hamming distance is', str(Haming_distance3), ', the percentage identity  of them is', ID3, '%.\n\n' )


                
            
            
    
