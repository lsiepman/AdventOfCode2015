import re

import numpy as np
import pandas as pd

# DATA
data = []
with open("./data/data_06.txt") as file:
    for line in file:
        data.append(line)

data = pd.DataFrame(data)

def FindAction(string):
    action = re.search(r"[a-z\s]*", string).group().strip()

    return action

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

# Part 1
lights = np.zeros((1000, 1000))

for row in range(len(data)):
    xfrom = data["Xfrom"][row]
    yfrom = data["Yfrom"][row]
    xto = data["Xto"][row] + 1
    yto = data["Yto"][row] + 1

    if data["Action"][row] == "turn on":
        lights[yfrom:yto, xfrom:xto] = 1
    elif data["Action"][row] == "turn off":
        lights[yfrom:yto, xfrom:xto] = 0
    elif data["Action"][row] == "toggle":
        lights[yfrom:yto, xfrom:xto] = np.where(
            lights[yfrom:yto, xfrom:xto] == 1,
            lights[yfrom:yto, xfrom:xto] - 1,
            lights[yfrom:yto, xfrom:xto] + 1,
        )
    else:
        print(row, "error")

print(f"Part 1: {int(lights.sum())}")

# Part 2
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

print(f"Part 2: {int(bright.sum())}")
