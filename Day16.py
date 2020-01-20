# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:40:09 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
import numpy as np
#%% GOAL 1
"""Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

    children, by human DNA age analysis.
    cats. It doesn't differentiate individual breeds.
    Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
    goldfish. No other kinds of fish.
    trees, all in one group.
    cars, presumably by exhaust or gasoline or something.
    perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?"""
#%% DATA
data = []
with open('Data - Day16.txt', 'r') as file:
    for line in file:
        data.append(line)

data = pd.DataFrame(data) 
#%% CALC 1
#cleaning all data
data = data[0].str.split(expand = True)
data[0] = data[0] + "_" + data[1].str.replace(":", "")
data.drop([1], axis = 1, inplace = True)
data[2] = data[2].str.replace(":", "")
data[3] = data[3].str.replace(",", "").astype(int)
data[4] = data[4].str.replace(":", "")
data[5] = data[5].str.replace(",", "").astype(int)
data[6] = data[6].str.replace(":", "")
data[7] = data[7].str.replace(",", "").astype(int)

df = pd.DataFrame(data[0])
df.columns = ["Sue"]
df["children"] = np.nan
df["cats"] = np.nan
df["samoyeds"] = np.nan
df["pomeranians"] = np.nan
df["akitas"] = np.nan
df["vizslas"] = np.nan
df["goldfish"] = np.nan
df["trees"] = np.nan
df["cars"] = np.nan
df["perfumes"] = np.nan

def CountCats(data, df, col1, col2):
    for i in range(len(data)):
        cat = data[col1].iloc[i]
        count = data[col2].iloc[i]
        
        df[cat].iloc[i] = count
    
    return df

df = CountCats(data, df, 2, 3)   
df = CountCats(data, df, 4, 5) 
df = CountCats(data, df, 6, 7)

df2 = df.copy()
#solving the riddle
df = df.loc[(df["children"] == 3) | (pd.isna(df["children"]))] 
df = df.loc[(df["cats"] == 7) | (pd.isna(df["cats"]))]
df = df.loc[(df["samoyeds"] == 2) | (pd.isna(df["samoyeds"]))]
df = df.loc[(df["pomeranians"] == 3) | (pd.isna(df["pomeranians"]))] 
df = df.loc[(df["akitas"] == 0) | (pd.isna(df["akitas"]))]
df = df.loc[(df["vizslas"] == 0) | (pd.isna(df["vizslas"]))]
df = df.loc[(df["goldfish"] == 5) | (pd.isna(df["goldfish"]))]
df = df.loc[(df["trees"] == 3) | (pd.isna(df["trees"]))] 
df = df.loc[(df["cars"] == 2) | (pd.isna(df["cars"]))]
df = df.loc[(df["perfumes"] == 1) | (pd.isna(df["perfumes"]))]

print(df["Sue"].iloc[0], "gave you the present")

#%% GOAL 2
"""As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?"""
#%% CALC 2
df2 = df2.loc[(df2["children"] == 3) | (pd.isna(df2["children"]))] 
df2 = df2.loc[(df2["cats"] > 7) | (pd.isna(df2["cats"]))]
df2 = df2.loc[(df2["samoyeds"] == 2) | (pd.isna(df2["samoyeds"]))]
df2 = df2.loc[(df2["pomeranians"] < 3) | (pd.isna(df2["pomeranians"]))] 
df2 = df2.loc[(df2["akitas"] == 0) | (pd.isna(df2["akitas"]))]
df2 = df2.loc[(df2["vizslas"] == 0) | (pd.isna(df2["vizslas"]))]
df2 = df2.loc[(df2["goldfish"] < 5) | (pd.isna(df2["goldfish"]))]
df2 = df2.loc[(df2["trees"] > 3) | (pd.isna(df2["trees"]))] 
df2 = df2.loc[(df2["cars"] == 2) | (pd.isna(df2["cars"]))]
df2 = df2.loc[(df2["perfumes"] == 1) | (pd.isna(df2["perfumes"]))]

print(df2["Sue"].iloc[0], "gave you the present")
