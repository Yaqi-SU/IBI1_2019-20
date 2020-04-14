# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 08:35:10 2020

@author: suyaqi
"""
#4.1Some simple math
a=518
b=518518
c=b/7
d=c/11
e=d/13
if a>e:
    print('a is greater than e')
elif a==b:
    print('a is equal to e')
else:
    print('e is greater than a')
# 4.2 booleans
    X=True
    Y=False
    Z=(X and not Y) or (Y and not X)
    W= (X!=Y)
if Z==W:
    print('W and Z are the same')
else:
    print('W and Z are not the same')
    
