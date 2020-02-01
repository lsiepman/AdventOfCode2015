# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 20:22:29 2020

@author: laura
"""

#%% IMPORTS
from itertools import combinations
from operator import mul
from functools import reduce
#%% DATA
packages = [1, 2, 3, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
#%% GOAL 1
"""***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***

What is the quantum entanglement of the first group of packages in the ideal configuration?"""
#%% CALC 1
print("goal weight =", sum(packages)/3) #520
all_combinations = [seq for i in range(len(packages), 0, -1) for seq in combinations(packages, i) if sum(seq) == 520]

len_all_combinations = [len(i) for i in all_combinations]
print(min(len_all_combinations))
indices_min = [index for index, value in enumerate(len_all_combinations) if value == 6]

short_combinations = [all_combinations[i] for i in indices_min]
quantum_short = [reduce(mul, i) for i in short_combinations]
print(min(quantum_short))
#%% GOAL 2
"""***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***"""

#%% CALC 2
print("goal weight =", sum(packages)/4) #390
all_combinations = [seq for i in range(len(packages), 0, -1) for seq in combinations(packages, i) if sum(seq) == 390]

len_all_combinations = [len(i) for i in all_combinations]
print(min(len_all_combinations))
indices_min = [index for index, value in enumerate(len_all_combinations) if value == 4]

short_combinations = [all_combinations[i] for i in indices_min]
quantum_short = [reduce(mul, i) for i in short_combinations]
print(min(quantum_short))
