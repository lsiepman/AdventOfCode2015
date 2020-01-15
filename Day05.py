# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 18:59:37 2020

@author: laura
"""

#%% GOALS - Part 1
"""Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    
How many strings are nice?
"""

#%% IMPORTS
import re
import pandas as pd
import numpy as np

#%% FUNCTIONS  - Part 1
def FindVowelLength(string):
    num_vowels = len(re.findall("[aeiou]", string))

    return num_vowels

def FindDoubleLetter(string):
    do_let = re.findall(r"(\w)(\1)", string)
    
    if len(do_let) > 0:
        result = "yes"
    else:
        result = "no"
    
    return result

def ForbiddenCombinations(string):
    matches = re.findall(r"ab|cd|pq|xy", string)

    if len(matches) > 0:
        result = "yes"
    else:
        result = "no"
    
    return result    


#%% DATA
data = pd.read_csv("Data - Day05.csv", header = None)

#%% CALCULATIONS - Part 1
data["vowels"] = data[0].apply(FindVowelLength)
data["double_letter"] = data[0].apply(FindDoubleLetter)
data["forbidden_combos"] = data[0].apply(ForbiddenCombinations)

conditions = [(data["vowels"] >= 3) & (data["double_letter"] == "yes") & (data["forbidden_combos"] == "no")]

data["nice"] = np.select(conditions, ["yes"], default = "no")

print("Number of nice", len(data.loc[data["nice"] == "yes"]))

#%% GOAL - Part 2
"""Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.


How many strings are nice under these new rules?"""


#%% CALCULATIONS - Part 2
nice = []
for row in data[0]:
    if re.search(r"([a-z])([a-z]).*(\1)(\2)", row):
        if re.search(r'([a-z])([a-z])(\1)', row):
            nice.append(row)

print("Number of nice", len(nice))        
