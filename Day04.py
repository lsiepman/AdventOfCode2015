# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 10:03:46 2020

@author: laura
"""

#%% GOALS - Part 1
"""***REMOVED***

***REMOVED***"""
#%% IMPORTS
from hashlib import md5
#%% DATA
example1 = "abcdef"
example2 = "609043"
data = b"iwrupvqb"

#%% CALCULATIONS - Part 1
example = example1 + example2
test = md5(example.encode())
print(test.hexdigest())

for i in range(1, 1000000):
    fullstr = data + str(i)
    hashed = md5(fullstr.encode())
    hashhex = hashed.hexdigest()
    
    if hashhex.startswith("00000"):
        print("hashhex:", hashhex)
        print("i:", i)
        break
    
print("The answer is", i)

#%% GOALS - Part 2
"""Now find one that starts with six zeroes."""
#%% CALCULATIONS - Part 2
for j in range(1, 100000000):
    fullstr = data + str(j)
    hashed = md5(fullstr.encode())
    hashhex = hashed.hexdigest()
    
    if hashhex.startswith("000000"):
        print("hashhex:", hashhex)
        print("The answer is", j)
        break
    
