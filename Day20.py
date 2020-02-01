# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 22:55:37 2020

@author: laura
"""

#%% IMPORTS

#%% GOAL 1
"""***REMOVED***

***REMOVED***

    ***REMOVED***
    ***REMOVED***
    ***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

***REMOVED***

***REMOVED***"""
#%% DATA
data = 34000000
#%% CALC1
def FindFactors(x):
    factors = []
    for i in range(1, x + 1):
       if x % i == 0:
           factors.append(i)
    
    return factors

def CalcPresents(list_of_factors, mult):
    presents = [mult * i for i in list_of_factors]
    total = sum(presents)
    
    return total

j = 750000
result = 0
while result < data:
    j += 1
    factors = FindFactors(j)
    result = CalcPresents(factors, 10)
    print(result)
    
print("House {0} will receive at least {1} presents".format(j, data))

#%% GOAL 2
"""***REMOVED***

***REMOVED***"""
#%% CALC 2
def SiftFactors(x, list_of_factors):
    sifted = []
    for i in list_of_factors:
        val = x/i
        
        if val < 50:
            sifted.append(i)
        
    return sifted


j = 750000
result = 0
while result < data:
    j+= 1
    factors = FindFactors(j)
    sifted_factors = SiftFactors(j, factors)
    result = CalcPresents(sifted_factors, 11)
    print(j, ":", result)

print("House {0} will receive at least {1} presents".format(j, data))
