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
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
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

#creates a dataframe 
df = pd.DataFrame(list(zip(names, odds,ips,arb1, lst2, oddslst2,ipb,arb2)), 
               columns =['Sky Name', 'Sky odds','imp %','arb1','Bet Name', 'Bet odd','imp %','arb2']) 
pd.set_option("display.max_rows", None, "display.max_columns", None)
#Removes all rows that contain a null value
df2 = df.dropna()
df2["Both Name"] = df2["Sky Name"] + " vs " + df["Bet Name"].shift(-1)
#printing all rows which satisfy the condition of a stat safe bet
safe = df2[(df2['arb1'] < 100)] 
safe.append(df2[(df2['arb2'] < 100)])
print(df)
#plotting the results to a bar chart
fig = go.Figure()
fig.add_trace(go.Bar(
    x=df2['Both Name'],
    y=df2['arb1'],
    text = df2['arb1'],
    name='arb1',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=df2['Both Name'],
    y=df2['arb2'],
    text = df2['arb2'],
    name='arb2',
    marker_color='lightsalmon'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.#
fig.update_layout(
    title="Betting arbitrage between Skybet and Betway",
    xaxis_title="Fighter 1 vs Fighter 2",
    yaxis_title="Arbitrage/%",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
plot(fig)
