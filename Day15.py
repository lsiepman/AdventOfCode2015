# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:32:30 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
from tqdm import tqdm
import itertools
#%% GOAL 1
"""Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

    capacity (how well it helps the cookie absorb milk)
    durability (how well it keeps the cookie intact when full of milk)
    flavor (how tasty it makes the cookie)
    texture (how it improves the feel of the cookie)
    calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

    A capacity of 44*-1 + 56*2 = 68
    A durability of 44*-2 + 56*3 = 80
    A flavor of 44*6 + 56*-2 = 152
    A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?


ANSWER = 13882464 (('Frosting', 'Sugar', 'Sprinkles', 'PeanutButter'), (18, 19, 28, 35))"""
#%% DATA
data = []
with open('Data - Day15.txt', 'r') as file:
    for line in file:
        data.append(line)

data = pd.DataFrame(data)

#%% CALC 1
data = data[0].str.split(expand = True)
data[0] = data[0].str.replace(":", "")
data = data.drop([1, 3, 5, 7, 9], axis = 1)
data[2] = data[2].str.replace(",", "")
data[4] = data[4].str.replace(",", "")
data[6] = data[6].str.replace(",", "")
data[8] = data[8].str.replace(",", "")
data.columns = ["Ingredient", "Capacity", "Durability", "Flavor", "Texture", "Calories"]

data[["Capacity", "Durability", "Flavor", "Texture", "Calories"]] = data[["Capacity", "Durability", "Flavor", "Texture", "Calories"]].astype(int)

def CalcScore(sprinkles, pb, frosting, sugar):
    cap1 = data.loc[data["Ingredient"] == "Sprinkles"]["Capacity"].iloc[0] * sprinkles
    cap2 = data.loc[data["Ingredient"] == "PeanutButter"]["Capacity"].iloc[0] * pb 
    cap3 = data.loc[data["Ingredient"] == "Frosting"]["Capacity"].iloc[0] * frosting 
    cap4 = data.loc[data["Ingredient"] == "Sugar"]["Capacity"].iloc[0] * sugar
    
    capacity = cap1 + cap2 + cap3 + cap4
    
    dur1 = data.loc[data["Ingredient"] == "Sprinkles"]["Durability"].iloc[0] * sprinkles   
    dur2 = data.loc[data["Ingredient"] == "PeanutButter"]["Durability"].iloc[0] * pb
    dur3 = data.loc[data["Ingredient"] == "Frosting"]["Durability"].iloc[0] * frosting
    dur4 = data.loc[data["Ingredient"] == "Sugar"]["Durability"].iloc[0] * sugar
     
    durability = dur1 + dur2 + dur3 + dur4
     
    fla1 = data.loc[data["Ingredient"] == "Sprinkles"]["Flavor"].iloc[0] * sprinkles 
    fla2 = data.loc[data["Ingredient"] == "PeanutButter"]["Flavor"].iloc[0] * pb 
    fla3 = data.loc[data["Ingredient"] == "Frosting"]["Flavor"].iloc[0] * frosting 
    fla4 = data.loc[data["Ingredient"] == "Sugar"]["Flavor"].iloc[0] * sugar
    
    flavor = fla1 + fla2 + fla3 + fla4
    
    tex1 = data.loc[data["Ingredient"] == "Sprinkles"]["Texture"].iloc[0] * sprinkles 
    tex2 = data.loc[data["Ingredient"] == "PeanutButter"]["Texture"].iloc[0] * pb 
    tex3 = data.loc[data["Ingredient"] == "Frosting"]["Texture"].iloc[0] * frosting 
    tex4 = data.loc[data["Ingredient"] == "Sugar"]["Texture"].iloc[0] * sugar
    
    texture = tex1 + tex2 + tex3 + tex4
    
    score = capacity * durability * flavor * texture
           
    return score
    
CalcScore(25, 25, 25, 25)


def sum_to_n(n, size, limit=None):
    """Produce all lists of `size` positive integers in decreasing order
    that add up to `n`."""
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail
            
four_nums = []            
for partition in sum_to_n(100, 4):
    four_nums.append(partition)

three_nums = []
for partition in sum_to_n(100, 3):
    three_nums.append(partition)
    
two_nums = []
for partition in sum_to_n(100, 2):
    two_nums.append(partition)
    
for i in three_nums:
    i.append(0)

for i in two_nums:
    i.append(0)
    i.append(0)

one_num = [[100, 0, 0, 0]]

all_number_combinations = one_num + two_nums + three_nums + four_nums    

all_nums = []
for i in tqdm(all_number_combinations):
    all_nums.append(list(itertools.permutations(i)))
    
combi_all = []
for i in all_nums:
    for j in i:
        combi_all.append(list(j))

combi_all.sort()
combi_all = list(combi_all for combi_all,_ in itertools.groupby(combi_all))

result = 0
for i in tqdm(combi_all[:50000]):
     new_result = CalcScore(i[0], i[1], i[2], i[3])
     if new_result > result:
        result = new_result.copy()
print("The highest cookie score is", result)

result = 0
for i in tqdm(combi_all[50000:100000]):
     new_result = CalcScore(i[0], i[1], i[2], i[3])
     if new_result > result:
        result = new_result.copy()       
print("The highest cookie score is", result)

result = 0
for i in tqdm(combi_all[100000:150000]):
     new_result = CalcScore(i[0], i[1], i[2], i[3])
     if new_result > result:
        result = new_result.copy()
print("The highest cookie score is", result)

result = 0
for i in tqdm(combi_all[150000:]):
     new_result = CalcScore(i[0], i[1], i[2], i[3])
     if new_result > result:
        result = new_result.copy()
print("The highest cookie score is", result)        

#%% GOAL 2
"""Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?"""

#%% CALC 2
def CalcScoreCalorie(sprinkles, pb, frosting, sugar):
    cap1 = data.loc[data["Ingredient"] == "Sprinkles"]["Capacity"].iloc[0] * sprinkles
    cap2 = data.loc[data["Ingredient"] == "PeanutButter"]["Capacity"].iloc[0] * pb 
    cap3 = data.loc[data["Ingredient"] == "Frosting"]["Capacity"].iloc[0] * frosting 
    cap4 = data.loc[data["Ingredient"] == "Sugar"]["Capacity"].iloc[0] * sugar
    
    capacity = cap1 + cap2 + cap3 + cap4
    
    dur1 = data.loc[data["Ingredient"] == "Sprinkles"]["Durability"].iloc[0] * sprinkles   
    dur2 = data.loc[data["Ingredient"] == "PeanutButter"]["Durability"].iloc[0] * pb
    dur3 = data.loc[data["Ingredient"] == "Frosting"]["Durability"].iloc[0] * frosting
    dur4 = data.loc[data["Ingredient"] == "Sugar"]["Durability"].iloc[0] * sugar
     
    durability = dur1 + dur2 + dur3 + dur4
     
    fla1 = data.loc[data["Ingredient"] == "Sprinkles"]["Flavor"].iloc[0] * sprinkles 
    fla2 = data.loc[data["Ingredient"] == "PeanutButter"]["Flavor"].iloc[0] * pb 
    fla3 = data.loc[data["Ingredient"] == "Frosting"]["Flavor"].iloc[0] * frosting 
    fla4 = data.loc[data["Ingredient"] == "Sugar"]["Flavor"].iloc[0] * sugar
    
    flavor = fla1 + fla2 + fla3 + fla4
    
    tex1 = data.loc[data["Ingredient"] == "Sprinkles"]["Texture"].iloc[0] * sprinkles 
    tex2 = data.loc[data["Ingredient"] == "PeanutButter"]["Texture"].iloc[0] * pb 
    tex3 = data.loc[data["Ingredient"] == "Frosting"]["Texture"].iloc[0] * frosting 
    tex4 = data.loc[data["Ingredient"] == "Sugar"]["Texture"].iloc[0] * sugar
    
    texture = tex1 + tex2 + tex3 + tex4
    
    cal1 = data.loc[data["Ingredient"] == "Sprinkles"]["Calories"].iloc[0] * sprinkles
    cal2 = data.loc[data["Ingredient"] == "PeanutButter"]["Calories"].iloc[0] * pb 
    cal3 = data.loc[data["Ingredient"] == "Frosting"]["Calories"].iloc[0] * frosting 
    cal4 = data.loc[data["Ingredient"] == "Sugar"]["Calories"].iloc[0] * sugar
    
    calories = cal1 + cal2 + cal3 + cal4
    
    score = capacity * durability * flavor * texture
    if calories == 500:       
        return score
    else:
        return 0
    
result = 0
for i in tqdm(combi_all[:50000]):
     new_result = CalcScoreCalorie(i[0], i[1], i[2], i[3])
     if new_result > result:
        result = new_result.copy()
print("The highest 500 Cal cookie score is", result)

result = 0
for i in tqdm(combi_all[50000:100000]):
     new_result = CalcScoreCalorie(i[0], i[1], i[2], i[3])
     if new_result > result:
        result = new_result.copy()       
print("The highest 500 Cal cookie score is", result)

result = 0
for i in tqdm(combi_all[100000:150000]):
     new_result = CalcScoreCalorie(i[0], i[1], i[2], i[3])
     if new_result > result:
        result = new_result.copy()
print("The highest 500 Cal cookie score is", result)

result = 0
for i in tqdm(combi_all[150000:]):
     new_result = CalcScoreCalorie(i[0], i[1], i[2], i[3])
     if new_result > result:
        result = new_result.copy()
print("The highest 500 Cal cookie score is", result)

