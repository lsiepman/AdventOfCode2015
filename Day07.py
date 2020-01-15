# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:18:04 2020

@author: laura
"""

#%% IMPORTS & SETTINGS
maximum = 65535 
import pandas as pd
import numpy as np
import re
from tqdm import tqdm

pd.set_option('mode.chained_assignment', None)
#%% GOALS 1
"""***REMOVED***

***REMOVED***

***REMOVED***

***REMOVED***"""
#%% DATA
data = []
with open('Data - Day07.txt', 'r') as file:
    for line in file:
        data.append(line)

data = pd.DataFrame(data)  

#%% EXAMPLES
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

#%% FUNCTIONS PART 1
def FindAssignedNum(string):
    if "AND" not in string:
        num = re.search("^\d*", string).group()
        if num == "":
            num = np.nan
        else: 
            num = int(num)
    else:
        num = np.nan
    return num

def FindOperation(string):
    op = re.search(r"\b[A-Z]{2,7}", string)
    if op == None:
        op = ""
    else:
        op = op.group()
    return op

def CalculateWires(data, maximum = 65535):
    for i in tqdm(range(len(data))):
        wireval = data["value_wire"][i]
        if pd.notna(wireval):
            continue
        
        input1 = data["input_wire_1"][i]
        inputval1 = data.loc[data["wire"] == input1]["value_wire"]
                
        if len(inputval1) == 0:
            inputval1 = np.nan
        else:
            inputval1 = inputval1.iloc[0]

        if input1 in [1, "1"]:
            inputval1 = 1            
        
        input2 = data["input_wire_2"][i]
        inputval2 = data.loc[data["wire"] == input2]["value_wire"]
        if len(inputval2) == 0:
            inputval2 = np.nan
        else:
            inputval2 = inputval2.iloc[0]
        operation = data["operation"][i]
        shift_value = data["shift_value"][i]
        
        if (operation == "AND" and pd.notna(inputval1) and pd.notna(inputval2)):
            data["value_wire"][i] = int(inputval1) & int(inputval2)
            
        elif(operation == "OR" and pd.notna(inputval1) and pd.notna(inputval2)):
            data["value_wire"][i] = int(inputval1) | int(inputval2)
            
        elif(operation == "NOT" and pd.notna(inputval1)):
            data["value_wire"][i] = maximum - int(inputval1)
        
        elif(operation == "RSHIFT" and pd.notna(inputval1)):
            data["value_wire"][i] = int(inputval1) >> int(shift_value)
        elif(operation == "LSHIFT" and pd.notna(inputval1)):
            data["value_wire"][i] = int(inputval1) << int(shift_value)
        else:
            continue
            
    return(data)
#%% CALCULATIONS PART 1
    
#preparing table
data["wire"] = data[0].str.split(" ").str[-1].str.strip()
data["value_wire"] = np.nan
data["input_wire_1"] = ""
data["input_wire_2"] = ""
data["shift_value"] = np.nan

data["operation"] = data[0].apply(FindOperation)

for row in range(len(data)):
    if data["operation"][row] in ["AND", "OR"]:
        data["input_wire_1"][row] = data[0][row].split(" ")[0]
        data["input_wire_2"][row] = data[0][row].split(" ")[2]
    elif data["operation"][row] in ["RSHIFT", "LSHIFT"]:
        data["shift_value"][row] = int(data[0][row].split(" ")[2])
        data["input_wire_1"][row] = data[0][row].split(" ")[0]
    else:
        data["input_wire_1"][row] = data[0][row].split(" ")[1]

#filling table
data["value_wire"] = data[0].apply(FindAssignedNum)

for i in range(1, 250):
    data = CalculateWires(data)


print("the signal provided to wire a =", data.loc[data["wire"] == "lx"]["value_wire"].iloc[0])

#%% GOAL PART 2
"""Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?"""

#%% CALCULATION 2
data["value_wire"] = np.nan
data["value_wire"] = data[0].apply(FindAssignedNum)
data.loc[data["wire"] == "b", ["value_wire"]] = 16076
for i in range(1, 250):
    data = CalculateWires(data)
    
print("the new signal provided to wire a =", data.loc[data["wire"] == "lx"]["value_wire"].iloc[0])
