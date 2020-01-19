# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:44:47 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
from collections import Counter
#%% GOAL 1
"""***REMOVED***

***REMOVED***

***REMOVED***

    ***REMOVED***
    ***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***"""
#%% DATA
data = []
with open('Data - Day14.txt', 'r') as file:
    for line in file:
        data.append(line)

data = pd.DataFrame(data)  
#%% CALC 1
data = data[0].str.split(expand = True)
data = data.drop([1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 14], axis = 1)
data.columns = ["Reindeer", "Speed", "Flies", "Rests"]
data[["Speed", "Flies", "Rests"]] = data[["Speed", "Flies", "Rests"]].astype(int)

test = data.iloc[0]
time = 2503
def DistFly(row, time):
    deer = row["Reindeer"]
    speed = row["Speed"]
    time_fly = row["Flies"]
    time_rest = row["Rests"]
    
    distance = 0
    both = time_fly + time_rest
    
    while time >= both:
        time = time - time_fly - time_rest
        distance = distance + speed * time_fly
    
    if time >= time_fly:
        time = time - time_fly
        distance = distance + speed * time_fly
    else: 
        distance = distance + speed * time
                   
    #print("{0} has flown {1} km after {2} seconds".format(deer, distance, 2503))
    
    return distance

distances = []
for i in range(len(data)):
    distances.append(DistFly(data.iloc[i], time))
    
print("The maximum flown distance is", max(distances))

#%% GOAL 2
"""***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***"""

#%% CALC 2
dist_all = []
for t in range(2503):
    distances = []
    for i in range(len(data)):
        distances.append(DistFly(data.iloc[i], t))
    dist_all.append(distances)

data["Score"] = 0
for i in dist_all:
    max_score = max(i)
    indices = [j for j,x in enumerate(i) if x == max_score]
    for k in indices:
        data["Score"].iloc[k] += 1


print("The highest score is", max(data["Score"])-1)
