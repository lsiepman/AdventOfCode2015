# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:35:19 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
import re
#%% GOAL 1
"""***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***
"""

#%% DATA
data = []
with open('Data - Day08.txt', 'r') as file:
    for line in file:
        data.append(line)

data = pd.DataFrame(data)  

#%% CALCULATION 1
#clean data
data[0] = data[0].str.strip()

# string literals
data["len_literal"] = data[0].apply(len)

def CleanString(string):
    step1 = re.sub(r"\\x[0-9A-Fa-f]{2}", "n", string)
    step2 = re.sub(r"\\{2}", "a", step1)
    step3 = re.sub(r"\\\"", "b", step2)
    step4 = re.sub(r"\"", "", step3)
    
    return step4

data["clean_string"] = data[0].apply(CleanString)
data["len_string"] = data["clean_string"].apply(len)

len_string = sum(data["len_string"])
len_lit = sum(data["len_literal"])
answer = len_lit - len_string
print("The answer is {}".format(answer))

#%% GOAL 2
"""***REMOVED***

***REMOVED***"""
#%% CALCULATIONS 2
def EncodeString(string):
    encoded = string
    encoded = encoded.replace("\\", "\\\\").replace('"', '\\"')
    encoded = '"' + encoded + '"'
    
    return len(encoded)

data["len_encoded"] = data[0].apply(EncodeString)
print("The second answer is {}".format(sum(data["len_encoded"]) - len_lit))
