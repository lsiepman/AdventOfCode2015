# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:49:03 2020

@author: laura
"""

#%% IMPORTS
import numpy as np
import pandas as pd
#%% GOAL 1
"""After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.

All of the lights update simultaneously; they all consider the same current state before moving to the next.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?"""
#%% DATA
data = []
with open("Data - Day18.txt", "r") as file:
    for line in file:
        data.append(line)
        
data = pd.DataFrame(data)
data = data[0].str.replace("#", "1 ").str.replace(".", "0 ")
data = pd.DataFrame(data)
data = data[0].str.split(expand = True)
data = np.array(data).astype(int)

data = np.pad(data, 1, "constant", constant_values = 0)
df = data.copy()
#%% CALC 1
def FindNeighbours(data):
    on = []
    off = []
    
    for y in range(1, 101):
        for x in range(1, 101):
    
            l = data[y, x]
            n1 = data[y+1, x-1]
            n2 = data[y+1, x]
            n3 = data[y+1, x+1]
            n4 = data[y, x+1]
            n5 = data[y-1, x+1]
            n6 = data[y-1, x]
            n7 = data[y-1, x-1]
            n8 = data[y, x-1]
            
            sum_n = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
        
            if l == 1 and sum_n in [2,3]:
                on.append((y, x))
            elif l == 1 and sum_n not in [2,3]:
                off.append((y, x))
            elif l == 0 and sum_n == 3:
                on.append((y, x))
            else:
                off.append((y, x))
    
    for a in on:
        data[a] = 1
    
    for b in off:
        data[b] = 0
    return data

for i in range(100):
    data = FindNeighbours(data)
    
print("After 100 steps {} lights will be on.".format(np.sum(data)))
#%% GOAL 2
"""You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?"""
#%% CALC 2
df[1,1] = 1
df[1, 100] = 1
df[100, 1] = 1
df[100, 100] = 1  

for j in range(100):
    df = FindNeighbours(df)
    df[1,1] = 1
    df[1, 100] = 1
    df[100, 1] = 1
    df[100, 100] = 1 

print("The number of lights that will be on after 100 steps:", np.sum(df))
