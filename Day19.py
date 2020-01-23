# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:11:12 2020

@author: laura
"""

#%% IMPORTS
import re
import pandas as pd
#%% GOAL 1
"""Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

"""
#%% DATA
text = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"

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
"""Now that the machine is calibrated, you're ready to begin molecule fabrication.

Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like the ones during calibration.

If you'd like to make HOH, you start with e, and then make the following replacements:

    e => O to get O
    O => HH to get HH
    H => OH (on the second H) to get HOH

So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.

How long will it take to make the medicine? Given the available replacements and the medicine molecule in your puzzle input, what is the fewest number of steps to go from e to the medicine molecule?
"""
#%% CALC 2
"""Bruteforcing this takes way too long"""
#https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju
print(sum(map(str.isupper,text)) - 2*text.count('Rn') - 2*text.count('Y') - 1)
