# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:41:33 2020

@author: laura
"""

# %% IMPORTS
import numpy as np
import pandas as pd
import re

# %% DATA
data = []
with open("Data - Day06.txt", "r") as file:
    for line in file:
        data.append(line)

data = pd.DataFrame(data)
# %% TESTING METHOD
example = np.zeros((10, 10))
example[4:6, 5:9] = 1

example[4:7, 5:7] = np.where(
    example[4:7, 5:7] == 1, example[4:7, 5:7] - 1, example[4:7, 5:7] + 1
)


# %% FUNCTIONS
def FindAction(string):
    action = re.search("[a-z\s]*", string).group().strip()

    return action


# %% CALCULATION 1
# clean instructions
data["Action"] = data[0].apply(FindAction)
data["Xfrom"] = data[0]
data["Yfrom"] = data[0]
data["Xto"] = data[0]
data["Yto"] = data[0]

data["Xfrom"] = (
    data["Xfrom"]
    .str.replace("turn on", "")
    .str.replace("turn off", "")
    .str.replace("toggle", "")
    .str.strip()
    .str.split(",")
    .str[0]
)
data["Yfrom"] = (
    data["Yfrom"]
    .str.replace("turn on", "")
    .str.replace("turn off", "")
    .str.replace("toggle", "")
    .str.strip()
    .str.split(",")
    .str[1]
    .str.split(" ")
    .str[0]
)
data["Xto"] = (
    data["Xto"]
    .str.replace("turn on", "")
    .str.replace("turn off", "")
    .str.replace("toggle", "")
    .str.strip()
    .str.split(",")
    .str[1]
    .str.split(" ")
    .str[2]
)
data["Yto"] = data["Yto"].str.split(",").str[-1]

for col in ["Xfrom", "Yfrom", "Xto", "Yto"]:
    data[col] = data[col].astype(int)

# Execute instructions
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
        lights[yfrom:yto, xfrom:xto] = np.where(
            lights[yfrom:yto, xfrom:xto] == 1,
            lights[yfrom:yto, xfrom:xto] - 1,
            lights[yfrom:yto, xfrom:xto] + 1,
        )
    else:
        print(row, "error")

print("Number of lights on:", lights.sum())

# %% Calculations 2
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
