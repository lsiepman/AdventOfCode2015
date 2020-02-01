# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:30:30 2020

@author: laura
"""

#%% IMPORTS

#%% DATA
row_data = 2947
col_data = 3029
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

#%% CALC 1
def CalcNextCode(code):
    return (code * 252533) % 33554393

def CalcSeq(input_row, input_col, code = 20151125):
    row = 1
    col = 1
    
    while True:
        if row == 1:
           row = col + 1
           col = 1
        else:
            row = row - 1
            col = col + 1
        
        code = CalcNextCode(code)
        if row == input_row and col == input_col:
            print(code)
            break

CalcSeq(row_data, col_data)
