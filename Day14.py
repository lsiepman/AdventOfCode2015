# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:44:47 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
from collections import Counter
#%% GOAL 1
"""This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

    Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?"""
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
"""Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?"""

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
