# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:12:08 2020

@author: laura
"""

#%% IMPORTS
import json
import re
from itertools import chain

#%% GOAL 1
"""Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

    [1,2,3] and {"a":2,"b":4} both have a sum of 6.
    [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
    {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
    [] and {} both have a sum of 0.

You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?"""

#%% DATA
with open("Data - Day12.json") as json_file:
    text = json_file.read()
    
with open("Data - Day12.json") as json_file:
    json_data = json.load(json_file)
    

#%% CALC 1
numbers = re.findall(r"[-0-9]+", text)    
total = 0
for i in numbers:
    total = total + int(i)

print("The sum of all numbers is", total)

#%% GOAL 2
"""Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

    [1,2,3] still has a sum of 6.
    [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
    {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
    [1,"red",5] has a sum of 6, because "red" in an array has no effect.
"""

#%% CALC 2
def Red(string):
  if "red" in string.values(): 
      return {}
  else: 
      return string

with open("Data - Day12.json") as json_file:
    cleaned_text = str(json.load(json_file, object_hook = Red))

cleaned_numbers = re.findall(r"[-0-9]+", cleaned_text) 
clean_calc = 0
for i in cleaned_numbers:
    clean_calc = clean_calc + int(i)

print("The sum off all non-red numbers is", clean_calc)
