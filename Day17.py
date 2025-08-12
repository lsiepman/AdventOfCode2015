# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:16:51 2020

@author: laura
"""

# %% IMPORTS
import itertools
from collections import Counter

# %% DATA
data = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
# %% CALC 1
result = [
    seq
    for i in range(len(data), 0, -1)
    for seq in itertools.combinations(data, i)
    if sum(seq) == 150
]
print("There are {} combinations".format(len(result)))

# %% CALC 2
lengths = []
for i in result:
    lengths.append(len(i))

print("The number of combinations with minimal containers is", Counter(lengths)[4])
