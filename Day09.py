# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:20:28 2020

@author: laura
"""

# %% imports
import pandas as pd
import itertools
from tqdm import tqdm

# %% data
data = []
with open("Data - Day09.txt", "r") as file:
    for line in file:
        data.append(line)

data = pd.DataFrame(data)


# %% calculation part 1
def Fro(string):
    return string.split(" ")[0]


def To(string):
    return string.split(" ")[2]


def Dist(string):
    return string.split(" ")[-1]


data["From"] = data[0].apply(Fro)
data["To"] = data[0].apply(To)
data["Distance"] = data[0].apply(Dist).astype(int)
data.drop(0, inplace=True, axis=1)

data2 = data.copy()
data2.columns = ["To", "From", "Distance"]
data = data.append(data2)
data.drop_duplicates(inplace=True)

list_of_places = list(data.From.unique()) + list(data.To.unique())
list_of_places = list(set(list_of_places))
unique_sequences = pd.DataFrame(itertools.permutations(list_of_places))
unique_sequences.columns = [
    "start",
    "step1",
    "step2",
    "step3",
    "step4",
    "step5",
    "step6",
    "end",
]


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

        dist1 = data.loc[
            (data["From"] == start) & (data["To"] == step1), ["Distance"]
        ].iloc[0]["Distance"]
        dist2 = data.loc[
            (data["From"] == step1) & (data["To"] == step2), ["Distance"]
        ].iloc[0]["Distance"]
        dist3 = data.loc[
            (data["From"] == step2) & (data["To"] == step3), ["Distance"]
        ].iloc[0]["Distance"]
        dist4 = data.loc[
            (data["From"] == step3) & (data["To"] == step4), ["Distance"]
        ].iloc[0]["Distance"]
        dist5 = data.loc[
            (data["From"] == step4) & (data["To"] == step5), ["Distance"]
        ].iloc[0]["Distance"]
        dist6 = data.loc[
            (data["From"] == step5) & (data["To"] == step6), ["Distance"]
        ].iloc[0]["Distance"]
        dist7 = data.loc[
            (data["From"] == step6) & (data["To"] == end), ["Distance"]
        ].iloc[0]["Distance"]

        dist_tot = dist1 + dist2 + dist3 + dist4 + dist5 + dist6 + dist7
        distances.append(dist_tot)

    return distances


dist_all = CalcDist(data, unique_sequences)

print("The shortest distance is", min(dist_all))


# %% CALCULATIONS 2
print("The longest distance is", max(dist_all))
