# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:30:01 2020

@author: a1nag
"""
from betway import f3t
from betway import oddt
from skybet import odds
from skybet import names
import pandas as pd 
import numpy as np 
from fractions import Fraction

#section of code that is used when skybet has boosters
#lst = []
#oddslst = []
#for i in range(0,len(names)-1):
 #   if ((len(names[i].split())) < 6 and (lst.count(names[i]) == 0)):
  #      lst.append(names[i])
   #     oddslst.append(odds[i])
#sorts the lists to match      
lst2 = [None] * len(names)
oddslst2 = [None] * len(odds)
for i in range(0,len(f3t)-1):
    if f3t[i] in names: 
        lst2[names.index(f3t[i])] = f3t[i]
        oddslst2[names.index(f3t[i])] = oddt[i]

#calculating implied probability
ipb = [None]*len(oddslst2)
ips = [None]*len(odds)
for i in range(0,len(oddslst2)-1):
    if oddslst2[i] is not None:
        ipb[i]=(1/(float(sum(Fraction(s) for s in oddslst2[i].split()))))*100
    
for i in range(0, len(odds)-1):
    print(odds[i])
    if odds[i] is not None and float(sum(Fraction(s) for s in odds[i].split())) != 0:
        ips[i] = (1/float(sum(Fraction(s) for s in odds[i].split())))*100
        print(i)

#Calculating arbitrage between skybet and betway
arb1 = [None]*len(odds)
arb2 = [None]*len(odds)
for i in range(0,len(odds)-1,2):
    if (oddslst2[i] is not None) and (oddslst2[i+1] is not None):
        arb1[i] = ips[i] + ipb[i+1]
        arb2[i] = ips[i+1] + ipb[i]

#creates a dataframe and prints it to terminal
df = pd.DataFrame(list(zip(names, odds,ips,arb1, lst2, oddslst2,ipb,arb2)), 
               columns =['Sky Name', 'Sky odds','imp %','arb1','Bet Name', 'Bet odd','imp %','arb2']) 
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)


#print(ipb, ' ',oddslst2,' ', ips)

