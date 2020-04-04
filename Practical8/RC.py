# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 08:59:30 2020

@author: suyaqi
"""

seq = 'ATGCGACTACGATCGAGGGCCAT'
re = seq[::-1]
reverse_seq = ''
for i in re:
    if i == 'A':
        reverse_seq+='T'
    elif i =='T':
        reverse_seq+='A'
    elif i =='C':
        reverse_seq+='G'
    elif i =='G':
        reverse_seq+='C'
print('The reverse complementary sequence of seq is',reverse_seq)
    
        