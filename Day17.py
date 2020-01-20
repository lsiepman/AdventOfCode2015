# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:16:51 2020

@author: laura
"""

#%% IMPORTS
import itertools
from collections import Counter
#%% GOAL 1
"""The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

    15 and 10
    20 and 5 (the first 5)
    20 and 5 (the second 5)
    15, 5, and 5

Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?"""
#%% DATA
data = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
#%% CALC 1
result = [seq for i in range(len(data), 0, -1) for seq in itertools.combinations(data, i) if sum(seq) == 150]
print("There are {} combinations".format(len(result)))
#%% GOAL 2
"""While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3."""
#%% CALC 2
lengths = []
for i in result:
    lengths.append(len(i))

print("The number of combinations with minimal containers is", Counter(lengths)[4])
