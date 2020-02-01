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
"""Little Jane Marie just got her very first computer for Christmas from some unknown benefactor. It comes with instructions and an example program, but the computer itself seems to be malfunctioning. She's curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six instructions (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named a and b, can hold any non-negative integer, and begin with a value of 0. The instructions are as follows:

    hlf r sets register r to half its current value, then continues with the next instruction.
    tpl r sets register r to triple its current value, then continues with the next instruction.
    inc r increments register r, adding 1 to it, then continues with the next instruction.
    jmp offset is a jump; it continues with the instruction offset away relative to itself.
    jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
    jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

All three jump instructions work with an offset relative to that instruction. The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively). For example, jmp +1 would simply continue with the next instruction, while jmp +0 would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:

inc a
jio a, +2
tpl a
inc a

What is the value in register b when the program in your puzzle input is finished executing?"""

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
"""The unknown benefactor is very thankful for releasi-- er, helping little Jane Marie with her computer. Definitely not to distract you, what is the value in register b after the program is finished executing if register a starts as 1 instead?"""

#%% CALC 2
a, b = FindAnswer(data, a = 1)
print("b =", b)