# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:38:31 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
import numpy as np
import itertools
from tqdm import tqdm
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

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83

***REMOVED***

***REMOVED***"""
#%% DATA
data = []
with open('Data - Day13.txt', 'r') as file:
    for line in file:
        data.append(line)

data = pd.DataFrame(data)  
#%% CALC 1
data = data[0].str.split(" ", expand = True)
data[3] = data[3].astype(int)
data[3] = np.where(data[2] == "lose", data[3]*-1, data[3])
data[10] = data[10].str.replace(".", "").str.replace("\n", "")

data = data.drop([1, 2, 4, 5, 6, 7, 8, 9], axis = 1)
data.columns = ["person1", "score", "person2"]

#seating orders
people = data["person1"].unique().tolist()
orders = pd.DataFrame(itertools.permutations(people))
orders.columns = ["start", "step1", "step2", "step3", "step4", "step5", "step6", "end"]

def CalcDist(data, df):
    distances = []
    for i in tqdm(range(len(df))):
        start = df["start"][i]
        step1 = df["step1"][i]
        step2 = df["step2"][i]
        step3 = df["step3"][i]
        step4 = df["step4"][i]
        step5 = df["step5"][i]
        step6 = df["step6"][i]
        end = df["end"][i]
        
        dist1 = data.loc[(data["person1"] == start) & (data["person2"] == step1), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == start) & (data["person1"] == step1), ["score"]].iloc[0]["score"]
        
        dist2 = data.loc[(data["person1"] == step1) & (data["person2"] == step2), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step1) & (data["person1"] == step2), ["score"]].iloc[0]["score"]
        
        dist3 = data.loc[(data["person1"] == step2) & (data["person2"] == step3), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step2) & (data["person1"] == step3), ["score"]].iloc[0]["score"]
        
        dist4 = data.loc[(data["person1"] == step3) & (data["person2"] == step4), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step3) & (data["person1"] == step4), ["score"]].iloc[0]["score"]
        
        dist5 = data.loc[(data["person1"] == step4) & (data["person2"] == step5), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step4) & (data["person1"] == step5), ["score"]].iloc[0]["score"]
        
        dist6 = data.loc[(data["person1"] == step5) & (data["person2"] == step6), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step5) & (data["person1"] == step6), ["score"]].iloc[0]["score"]
        
        dist7 = data.loc[(data["person1"] == step6) & (data["person2"] == end), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step6) & (data["person1"] == end), ["score"]].iloc[0]["score"]
        
        dist8 = data.loc[(data["person1"] == end) & (data["person2"] == start), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == end) & (data["person1"] == start), ["score"]].iloc[0]["score"]
        
        dist_tot = dist1 + dist2 + dist3 + dist4 + dist5 + dist6 + dist7 + dist8
        distances.append(dist_tot)
    
    return distances

dist_all = CalcDist(data, orders)
orders["scores"] = dist_all
print("The highest score is", max(dist_all))

#%% GOAL 2
"""***REMOVED***

***REMOVED***

***REMOVED***"""

#%% CALC2
data2 = pd.DataFrame(list(zip(["Me", "Me", "Me", "Me", "Me", "Me", "Me", "Me", "Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory"], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ["Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory","Me", "Me", "Me", "Me", "Me", "Me", "Me", "Me"])), columns = ["person1", "score", "person2"])

data = data.append(data2, ignore_index = True)

#seating orders
people2 = data["person1"].unique().tolist()
orders2 = pd.DataFrame(itertools.permutations(people2))
orders2.columns = ["start", "step1", "step2", "step3", "step4", "step5", "step6", "step7", "end"]

def CalcDist2(data, df):
    distances = []
    for i in tqdm(range(len(df))):
        start = df["start"][i]
        step1 = df["step1"][i]
        step2 = df["step2"][i]
        step3 = df["step3"][i]
        step4 = df["step4"][i]
        step5 = df["step5"][i]
        step6 = df["step6"][i]
        step7 = df["step7"][i]
        end = df["end"][i]
        
        dist1 = data.loc[(data["person1"] == start) & (data["person2"] == step1), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == start) & (data["person1"] == step1), ["score"]].iloc[0]["score"]
        
        dist2 = data.loc[(data["person1"] == step1) & (data["person2"] == step2), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step1) & (data["person1"] == step2), ["score"]].iloc[0]["score"]
        
        dist3 = data.loc[(data["person1"] == step2) & (data["person2"] == step3), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step2) & (data["person1"] == step3), ["score"]].iloc[0]["score"]
        
        dist4 = data.loc[(data["person1"] == step3) & (data["person2"] == step4), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step3) & (data["person1"] == step4), ["score"]].iloc[0]["score"]
        
        dist5 = data.loc[(data["person1"] == step4) & (data["person2"] == step5), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step4) & (data["person1"] == step5), ["score"]].iloc[0]["score"]
        
        dist6 = data.loc[(data["person1"] == step5) & (data["person2"] == step6), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step5) & (data["person1"] == step6), ["score"]].iloc[0]["score"]
        
        dist7 = data.loc[(data["person1"] == step6) & (data["person2"] == step7), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step6) & (data["person1"] == step7), ["score"]].iloc[0]["score"]
        
        dist8 = data.loc[(data["person1"] == step7) & (data["person2"] == end), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == step7) & (data["person1"] == end), ["score"]].iloc[0]["score"]
        
        dist9 = data.loc[(data["person1"] == end) & (data["person2"] == start), ["score"]].iloc[0]["score"] + data.loc[(data["person2"] == end) & (data["person1"] == start), ["score"]].iloc[0]["score"]
        
        dist_tot = dist1 + dist2 + dist3 + dist4 + dist5 + dist6 + dist7 + dist8 + dist9
        distances.append(dist_tot)
    
    return distances

dist_all2 = CalcDist2(data, orders2)

print("The highest score is",  max(dist_all2))
