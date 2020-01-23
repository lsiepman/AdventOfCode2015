# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:11:12 2020

@author: laura
"""

#%% IMPORTS
import re
import pandas as pd
#%% GOAL 1
"""***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***

"""
#%% DATA
text = "***REMOVED***"

data = []
with open("Data - Day19.txt", "r") as file:
    for line in file:
        data.append(line)
data = pd.DataFrame(data)
#%% CALC 1
medicine = re.findall("[A-Ze][^A-Ze]*", text)
data = data[0].str.replace("\n", "").str.split("=>", expand = True)
data[0] = data[0].str.strip()
data[1] = data[1].str.strip()
data.columns = ["FROM", "TO"]


    
    


replacements = []
for i in range(len(data)):
    FROM = data["FROM"].iloc[i] 
    TO = data["TO"].iloc[i]
    
    indices =  [k for k, x in enumerate(medicine) if x == FROM]
    for j in indices:
        changed = medicine.copy()
        changed[j] = TO
        replacements.append(changed)

for l in range(len(replacements)):
    replacements[l] = "".join(replacements[l])

replacements = list(set(replacements))

print("The number of different medicine is:", len(replacements))

#%% GOAL 2
"""***REMOVED***

***REMOVED***

***REMOVED***

    ***REMOVED***
    ***REMOVED***
    ***REMOVED***

***REMOVED***

***REMOVED***
"""
#%% CALC 2
"""Bruteforcing this takes way too long"""
#https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju
print(sum(map(str.isupper,text)) - 2*text.count('Rn') - 2*text.count('Y') - 1)
