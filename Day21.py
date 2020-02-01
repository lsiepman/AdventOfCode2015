# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:09:09 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
import itertools
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
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***

***REMOVED***

***REMOVED***"""

#%% DATA
data = {"Hit Points" : 100, "Damage" : 8, "Armor" : 2}
shop = pd.DataFrame(list(zip(["Dagger", "Shortsword", "Warhammer", "Longsword", "Greataxe", "Leather", "Chainmail", "Splitmail", "Bandedmail", "Platemail", "Damage1", "Damage2", "Damage3", "Defense1", "Defense2", "Defense3"], [8, 10, 25, 40, 74, 13, 31, 53, 75, 102, 25, 50, 100, 20, 40, 80], [4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0], [0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 0, 0, 0, 1, 2, 3])), columns = ["Item", "Cost", "Damage", "Armor"])
#%% CALC 1
"""To win, you need to do more damage than the boss every turn. You need to buy the cheapest items to do that"""

#DATA PREP
weapons = shop.iloc[0:5, :]
armor = shop.iloc[5:10, :]
rings = shop.iloc[10:16]
no_rings = pd.DataFrame(list(zip(["No1", "No2"], [0, 0], [0,0], [0,0])), columns = rings.columns)
rings = rings.append(no_rings, ignore_index = True)
armor = armor.append(pd.DataFrame(list(zip(["No"], [0], [0], [0])), columns = armor.columns), ignore_index = True)

result = pd.DataFrame(columns = ["Weapon", "Armor", "Ring1", "Ring2", "Costs", "Wins"])

combinations = []
for combination in itertools.product(weapons.Item.tolist(), armor.Item.tolist(), rings.Item.tolist(),rings.Item.tolist()):
    if combination[2] != combination[3]:
        combinations.append(combination)

#SIMULATING THE BATTLE
def SimulateFight(weapon, armor_item, ring1, ring2, result, nr):
    boss_hp = 100
    boss_dam = 8
    boss_arm = 2

    hp = 100
    damage = weapons.loc[weapons["Item"] == weapon]["Damage"].iloc[0] + rings.loc[rings["Item"] == ring1]["Damage"].iloc[0] + rings.loc[rings["Item"] == ring2]["Damage"].iloc[0]
    defense = armor.loc[armor["Item"] == armor_item]["Armor"].iloc[0] + rings.loc[rings["Item"] == ring1]["Armor"].iloc[0] + rings.loc[rings["Item"] == ring2]["Armor"].iloc[0]
    
    while boss_hp > 0 and hp > 0:
        boss_hp = boss_hp - (damage - boss_arm)
        if boss_hp <= 0:
            win = "player"
            break
        hp = hp - (boss_dam - defense)
        win = "boss"
        
    costs = weapons.loc[weapons["Item"] == weapon]["Cost"].iloc[0] + rings.loc[rings["Item"] == ring1]["Cost"].iloc[0] + rings.loc[rings["Item"] == ring2]["Cost"].iloc[0] + armor.loc[armor["Item"] == armor_item]["Cost"].iloc[0]
    
    result.loc[nr] = [weapon, armor_item, ring1, ring2, costs, win]
    
    return result

for i in range(len(combinations)):
    result = SimulateFight(combinations[i][0], combinations[i][1], combinations[i][2], combinations[i][3], result, i)

answer = result.loc[result["Wins"] == "player"]

print("The cheapest win is", min(answer["Costs"]))
    
#%% GOAL 2
"""***REMOVED***

***REMOVED***"""
#%% CALC 2
answer2 = result.loc[result["Wins"] == "boss"]
print("The most expensive way to lose is", max(answer2["Costs"]))
