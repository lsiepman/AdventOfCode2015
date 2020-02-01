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
"""It's Christmas Eve, and Santa is loading up the sleigh for this year's deliveries. However, there's one small problem: he can't get the sleigh to balance. If it isn't balanced, he can't defy physics, and nobody gets presents this year.

No pressure.

Santa has provided you a list of the weights of every package he needs to fit on the sleigh. The packages need to be split into three groups of exactly the same weight, and every package has to fit. The first group goes in the passenger compartment of the sleigh, and the second and third go in containers on either side. Only when all three groups weigh exactly the same amount will the sleigh be able to fly. Defying physics has rules, you know!

Of course, that's not the only problem. The first group - the one going in the passenger compartment - needs as few packages as possible so that Santa has some legroom left over. It doesn't matter how many packages are in either of the other two groups, so long as all of the groups weigh the same.

Furthermore, Santa tells you, if there are multiple ways to arrange the packages such that the fewest possible are in the first group, you need to choose the way where the first group has the smallest quantum entanglement to reduce the chance of any "complications". The quantum entanglement of a group of packages is the product of their weights, that is, the value you get when you multiply their weights together. Only consider quantum entanglement if the first group has the fewest possible number of packages in it and all groups weigh the same amount.

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
"""That's weird... the sleigh still isn't balancing.

"Ho ho ho", Santa muses to himself. "I forgot the trunk".

Balance the sleigh again, but this time, separate the packages into four groups instead of three. The other constraints still apply.

Now, what is the quantum entanglement of the first group of packages in the ideal configuration?"""

#%% CALC 2
print("goal weight =", sum(packages)/4) #390
all_combinations = [seq for i in range(len(packages), 0, -1) for seq in combinations(packages, i) if sum(seq) == 390]

len_all_combinations = [len(i) for i in all_combinations]
print(min(len_all_combinations))
indices_min = [index for index, value in enumerate(len_all_combinations) if value == 4]

short_combinations = [all_combinations[i] for i in indices_min]
quantum_short = [reduce(mul, i) for i in short_combinations]
print(min(quantum_short))
