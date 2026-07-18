# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 18:59:37 2020

@author: laura
"""

# %% GOALS - Part 1
"""
How many strings are nice?
"""

# %% IMPORTS
import re
import pandas as pd
import numpy as np


# %% FUNCTIONS  - Part 1
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


# %% DATA
data = pd.read_csv("Data - Day05.csv", header=None)

# %% CALCULATIONS - Part 1
data["vowels"] = data[0].apply(FindVowelLength)
data["double_letter"] = data[0].apply(FindDoubleLetter)
data["forbidden_combos"] = data[0].apply(ForbiddenCombinations)

conditions = [
    (data["vowels"] >= 3)
    & (data["double_letter"] == "yes")
    & (data["forbidden_combos"] == "no")
]

data["nice"] = np.select(conditions, ["yes"], default="no")

print("Number of nice", len(data.loc[data["nice"] == "yes"]))


# %% CALCULATIONS - Part 2
nice = []
for row in data[0]:
    if re.search(r"([a-z])([a-z]).*(\1)(\2)", row):
        if re.search(r"([a-z])([a-z])(\1)", row):
            nice.append(row)

print("Number of nice", len(nice))
