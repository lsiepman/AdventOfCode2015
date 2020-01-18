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
"""In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83

After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?"""
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
"""In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?"""

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
