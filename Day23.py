# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:37:36 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
import re
import numpy as np
#%% GOAL 1
"""***REMOVED***

***REMOVED***

    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

***REMOVED***"""

#%% DATA
data = []
with(open("Data - Day23.txt", "r")) as file:
    for line in file:
        data.append(line)
        
data = pd.DataFrame(data, columns = ["all"])
#%% CALC 1
def FindAction(string):
    return re.search(r"^[a-z]{3}", string).group()

def FindRegister(string):
    try:
        return re.search(r"[ab]", string).group()
    except AttributeError:
        return ""

def FindNum(string):
    try:
        return int(re.search(r"[\-0-9]{1,2}", string).group())
    except AttributeError:
        return np.nan

data["action"] = data["all"].apply(FindAction)
data["register"] = data["all"].apply(FindRegister)
data["number"] = data["all"].apply(FindNum)

def FindAnswer(data, a = 0, b = 0):
    i = 0
    while i < len(data):
        action = data["action"][i]
        register = data["register"][i]
        num = data["number"][i]
        
        if action == "inc" and register == "a":
            a += 1
        elif action == "inc" and register == "b":
            b += 1
        elif action == "hlf" and register == "a":
            a = a/2
        elif action == "hlf" and register == "b":
            b = b/2
        elif action == "tpl" and register == "a":
            a = a*3
        elif action == "tpl" and register == "b":
            b = b*3
        elif action == "jio" and register == "a":
            if a == 1:
                i = i + num
                continue
        elif action == "jio" and register == "b":
            if b == 1:
                i = i + num
                continue
        elif action == "jie" and register == "a":
            if (a % 2) == 0:
                i = i + num
                continue
        elif action == "jie" and register == "b":
            if (b % 2) == 0:
                i = i + num
                continue
        elif action == "jmp":
            i = i + num
            continue
        else: print("unknown")
        
        i += 1
        
    return a, b

a, b = FindAnswer(data)
print("b =", b)

#%% GOAL 2
"""***REMOVED***"""

#%% CALC 2
a, b = FindAnswer(data, a = 1)
print("b =", b)