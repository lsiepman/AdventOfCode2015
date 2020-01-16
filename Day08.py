# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:35:19 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
import re
#%% GOAL 1
"""Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.

It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.

Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are [double backslash] (which represents a single backslash), [single backslash double-quote] (which represents a lone double-quote character), and [single backslash x] plus two hexadecimal characters (which represents a single character with that ASCII code).

Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?
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
"""Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code representation as a new string and find the number of characters of the new encoded representation, including the surrounding double quotes.

Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal."""
#%% CALCULATIONS 2
def EncodeString(string):
    encoded = string
    encoded = encoded.replace("\\", "\\\\").replace('"', '\\"')
    encoded = '"' + encoded + '"'
    
    return len(encoded)

data["len_encoded"] = data[0].apply(EncodeString)
print("The second answer is {}".format(sum(data["len_encoded"]) - len_lit))
