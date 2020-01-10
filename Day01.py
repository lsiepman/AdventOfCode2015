# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:16:39 2020

@author: laura
"""
#%% GOAL - Part 1
"""***REMOVED***

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

To what floor do the instructions take Santa?"""

#%% IMPORTS
import re
#%% SETTINGS

#%% DATA
data = r"***REMOVED***"

#%% CALCULATIONS - Part 1
up = len(re.findall("\(", data))
down = len(re.findall("\)", data))
floor = up - down
print("floor =", floor)

#%% GOAL- Part 2
"""Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

What is the position of the character that causes Santa to first enter the basement? """

#%% CALCULATIONS - Part 2
now = 0
i = 0
while now != -1:
    if re.search("\(", data[i]):
        now += 1
    else:
        now -=1
    
    i += 1

print("position =", i) #python indexes from 0, but you add an additional one at the end
