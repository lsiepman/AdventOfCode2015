# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:09:09 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
import itertools
#%% GOAL 1
"""Little Henry Case got a new video game for Christmas. It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop. He hands you the controller.

In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points. If the defender had an armor score of 300, the defender would still lose 1 hit point.

Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items. You have 100 hit points.

Here is what the item shop is selling:

Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3

You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:

    The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
    The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
    The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
    The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
    The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
    The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
    The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.

In this scenario, the player wins! (Barely.)

You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?"""

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
"""Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants. The other rules still apply, and he still only has one of each item.

What is the most amount of gold you can spend and still lose the fight?"""
#%% CALC 2
answer2 = result.loc[result["Wins"] == "boss"]
print("The most expensive way to lose is", max(answer2["Costs"]))
