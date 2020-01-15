# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:41:33 2020

@author: laura
"""

#%% GOAL 1
"""Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

After following the instructions, how many lights are lit?"""

#%% IMPORTS
import numpy as np
import pandas as pd
import re
#%% DATA
data = []
with open('Data - Day06.txt', 'r') as file:
    for line in file:
        data.append(line)

data = pd.DataFrame(data)        
#%% TESTING METHOD
example = np.zeros((10, 10))
example[4:6, 5:9] = 1

example[4:7, 5:7] = np.where(example[4:7, 5:7] == 1, example[4:7, 5:7]-1, example[4:7, 5:7]+1)

#%% FUNCTIONS
def FindAction(string):
    action = re.search("[a-z\s]*", string).group().strip()
    
    return action

#%% CALCULATION 1
#clean instructions
data["Action"] = data[0].apply(FindAction)
data["Xfrom"] = data[0]
data["Yfrom"] = data[0]
data["Xto"] = data[0]
data["Yto"] = data[0]

data["Xfrom"] = data["Xfrom"].str.replace("turn on", "").str.replace("turn off", "").str.replace("toggle", "").str.strip().str.split(",").str[0]
data["Yfrom"] = data["Yfrom"].str.replace("turn on", "").str.replace("turn off", "").str.replace("toggle", "").str.strip().str.split(",").str[1].str.split(" ").str[0]
data["Xto"] = data["Xto"].str.replace("turn on", "").str.replace("turn off", "").str.replace("toggle", "").str.strip().str.split(",").str[1].str.split(" ").str[2]
data["Yto"] = data["Yto"].str.split(",").str[-1]

for col in ["Xfrom", "Yfrom", "Xto", "Yto"]:
   data[col] = data[col].astype(int)

#Execute instructions
lights = np.zeros((1000, 1000))

for row in range(len(data)):
    xfrom = data["Xfrom"][row]
    yfrom = data["Yfrom"][row]
    xto = data["Xto"][row] + 1
    yto = data["Yto"][row] + 1
    
    if data["Action"][row] == "turn on":
        print(row, "on")
        lights[yfrom:yto, xfrom:xto] = 1
    elif data["Action"][row] == "turn off":
        print(row, "off")
        lights[yfrom:yto, xfrom:xto] = 0
    elif data["Action"][row] == "toggle":
        print(row, "toggle")
        lights[yfrom:yto, xfrom:xto] = np.where(lights[yfrom:yto, xfrom:xto] == 1, lights[yfrom:yto, xfrom:xto] - 1, lights[yfrom:yto, xfrom:xto] + 1)
    else:
        print(row, "error")

print("Number of lights on:", lights.sum())

#%% GOALS PART 2
"""You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?"""

#%% Calculations 2
bright = np.zeros((1000, 1000))

for row in range(len(data)):
    xfrom = data["Xfrom"][row]
    yfrom = data["Yfrom"][row]
    xto = data["Xto"][row] + 1
    yto = data["Yto"][row] + 1
    
    if data["Action"][row] == "turn on":
        bright[yfrom:yto, xfrom:xto] += 1
    elif data["Action"][row] == "turn off":
        bright[yfrom:yto, xfrom:xto] -= 1
        bright = np.where(bright == -1, 0, bright)
    elif data["Action"][row] == "toggle":
       bright[yfrom:yto, xfrom:xto] += 2
    else:
        print(row, "error")

print("Total brightness of lights:", bright.sum())
