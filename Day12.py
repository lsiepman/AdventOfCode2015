# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:12:08 2020

@author: laura
"""

# %% IMPORTS
import json
import re
from itertools import chain


# %% DATA
with open("Data - Day12.json") as json_file:
    text = json_file.read()

with open("Data - Day12.json") as json_file:
    json_data = json.load(json_file)


# %% CALC 1
numbers = re.findall(r"[-0-9]+", text)
total = 0
for i in numbers:
    total = total + int(i)

print("The sum of all numbers is", total)


# %% CALC 2
def Red(string):
    if "red" in string.values():
        return {}
    else:
        return string


with open("Data - Day12.json") as json_file:
    cleaned_text = str(json.load(json_file, object_hook=Red))

cleaned_numbers = re.findall(r"[-0-9]+", cleaned_text)
clean_calc = 0
for i in cleaned_numbers:
    clean_calc = clean_calc + int(i)

print("The sum off all non-red numbers is", clean_calc)
