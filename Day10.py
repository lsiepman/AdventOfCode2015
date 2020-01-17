# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 23:37:22 2020

@author: laura
"""

#%% IMPORTS
from itertools import groupby
#%% GOAL 1
"""***REMOVED***

***REMOVED***

For example:

    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***

***REMOVED***"""
#%% DATA
data = "1321131112"

#%% CALC 1
seq = data
for i in range(40):
    string = []
    for k, g in groupby(seq):
        output = str(len(list(g))) + k
        string.append(output)
    seq = "".join(string)    
    
print("The answer is", len(seq))


#%% GOAL 2
"""***REMOVED***

***REMOVED***"""

#%% CALC 2
seq = data
for i in range(50):
    string = []
    for k, g in groupby(seq):
        output = str(len(list(g))) + k
        string.append(output)
    seq = "".join(string)    
    
print("The answer is", len(seq))