# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:18:20 2020

@author: suyaqi
"""
print('It may take some time to process, thanks for waiting :)')
#Import necessary libraries
import pandas as pd
import xml.dom.minidom as xdm
#define a function to find the number of childnodes
def childnode(n1):
    global terms
    childnodes=0#Count the childnodes
    #get 'is_a'
    for term in terms:
        is_a=term.getElementsByTagName('is_a')
        for parent in is_a:
            #if n1 is parent
            if parent.childNodes[0].data==n1:
                childnodes+=1
                #count childnodes of the childnode
                n2=term.getElementsByTagName('id')[0].childNodes[0].data
                childnodes+=childnode(n2)
    return childnodes
Id=[]#A list to store id
Name=[]#A list to store name
definition=[]#A list to store 'defstr'
childnodes=[]#A list to store number of nodes
domtree=xdm.parse('go_obo.xml')
dom=domtree.documentElement
#get all terms
terms=dom.getElementsByTagName('term')
#get all contents in <defstr>
for term in terms:
    defs=term.getElementsByTagName('def')[0]
    defstr=defs.getElementsByTagName('defstr')[0].childNodes[0].data
    #if 'autophagosome' is found
    if defstr.find('autophagosome')>-1 or defstr.find('Autophagosome')>-1:
        #get id, name, definition and add them to the lists 
        n1=term.getElementsByTagName('id')[0].childNodes[0].data
        Id.append(n1)
        Name.append(term.getElementsByTagName('name')[0].childNodes[0].data)
        definition.append(defstr)
        #get the number of childnodes and add to the list
        childnodes.append(childnode(n1))
#output the data into an excel file
data={'id':Id,'Name':Name,'definition':definition,'childnodes':childnodes}
dataframe=pd.DataFrame(data)
dataframe.to_excel(r'C:\Users\suyaqi\Desktop\IBI1\IBI1_2019-20\Practical14\autophagosome.xlsx')
print('The file has been created successfully!')

