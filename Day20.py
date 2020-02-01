# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 22:55:37 2020

@author: laura
"""

#%% IMPORTS

#%% GOAL 1
"""To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on that number:

    The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
    The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
    Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....

There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to ten times his or her number at each house.

So, the first nine houses on the street end up like this:

House 1 got 10 presents. -> 10
House 2 got 30 presents. -> 10 + 20
House 3 got 40 presents. -> 10 + 30
House 4 got 70 presents. -> 10 + 20 + 40
House 5 got 60 presents. -> 10 + 50
House 6 got 120 presents. -> 10 + 20 + 30 + 60
House 7 got 80 presents. -> 10 + 70
House 8 got 150 presents. -> 10 + 20 + 40 + 80
House 9 got 130 presents. -> 10 + 30 + 90

The first house gets 10 presents: it is visited only by Elf 1, which delivers 1 * 10 = 10 presents. The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?"""
#%% DATA
data = 34000000
#%% CALC1
def FindFactors(x):
    factors = []
    for i in range(1, x + 1):
       if x % i == 0:
           factors.append(i)
    
    return factors

def CalcPresents(list_of_factors, mult):
    presents = [mult * i for i in list_of_factors]
    total = sum(presents)
    
    return total

j = 750000
result = 0
while result < data:
    j += 1
    factors = FindFactors(j)
    result = CalcPresents(factors, 10)
    print(result)
    
print("House {0} will receive at least {1} presents".format(j, data))

#%% GOAL 2
"""The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to 50 houses. To make up for it, they decide to deliver presents equal to eleven times their number at each house.

With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?"""
#%% CALC 2
def SiftFactors(x, list_of_factors):
    sifted = []
    for i in list_of_factors:
        val = x/i
        
        if val < 50:
            sifted.append(i)
        
    return sifted


j = 750000
result = 0
while result < data:
    j+= 1
    factors = FindFactors(j)
    sifted_factors = SiftFactors(j, factors)
    result = CalcPresents(sifted_factors, 11)
    print(j, ":", result)

print("House {0} will receive at least {1} presents".format(j, data))
