# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:40:09 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
import numpy as np
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
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

***REMOVED***

***REMOVED***"""
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
"""***REMOVED***

***REMOVED***

***REMOVED***"""
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
