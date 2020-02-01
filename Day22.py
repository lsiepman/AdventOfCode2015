# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:02:31 2020

@author: laura

credit to https://www.reddit.com/r/adventofcode/comments/3xspyl/day_22_solutions/cy7mbfz/ 
"""

#%% IMPORTS
from copy import deepcopy
#%% GOAL 1
"""Little Henry Case decides that defeating bosses with swords and stuff is boring. Now he's playing the game with a wizard. Of course, he gets stuck on another boss and needs your help again.

In this version, combat still proceeds with the player and the boss taking alternating turns. The player still goes first. Now, however, you don't get any equipment; instead, you must choose one of your spells to cast. The first character at or below 0 hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack normally. However, since you do magic damage, your opponent's armor is ignored, and so the boss effectively has zero armor as well. As before, if armor (from a spell, in this case) would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always deal at least 1 damage.

On each of your turns, you must select one of your spells to cast. If you cannot afford to cast any spell, you lose. Spells cost mana; you start with 500 mana, but have no maximum limit. You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

    Magic Missile costs 53 mana. It instantly does 4 damage.
    Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
    Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
    Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
    Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

Effects all work the same way. Effects apply at the start of both the player's turns and the boss' turns. Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one. If this decreases the timer to zero, the effect ends. You cannot cast a spell that would start an effect which is already active. However, effects can be started on the same turn they end.

You start with 50 hit points and 500 mana points. The boss's actual stats are in your puzzle input. What is the least amount of mana you can spend and still win the fight? (Do not include mana recharge effects as "spending" negative mana.)"""

#%% DATA
missile = {"mana": 53, "damage": 4, "heal" : 0, "armor": 0, "recharge" :0, "active" : 0, "nr": 0}
drain = {"mana": 73, "damage": 2, "heal" : 2, "armor": 0, "recharge" :0, "active" : 0, "nr": 1}
shield = {"mana": 113, "damage": 0, "heal" : 0, "armor": 7, "recharge" :0, "active" : 6, "nr": 2}
poison = {"mana": 173, "damage": 3, "heal" : 0, "armor": 0, "recharge" :0, "active" : 6, "nr": 3}
recharge = {"mana": 229, "damage": 0, "heal" : 0, "armor": 0, "recharge" :101, "active" : 5, "nr": 4}
spells = [missile, drain, shield, poison, recharge]

#%% SOLUTION 1
ManaMinimum = 10000 #just chose a random number sufficiently large

def Battle(boss_hp, hp, mana, lasting_spells, turn, mana_spent):
    boss_damage = 9
    armor = 0
    
    #        
    cast_spells = []
    for lasting_spell in lasting_spells:
        if lasting_spell[5] >= 0: 
            boss_hp -= lasting_spell[1]
            hp += lasting_spell[2]
            armor += lasting_spell[3]
            mana += lasting_spell[4]

        cast_spell = [lasting_spell[0], lasting_spell[1], lasting_spell[2], lasting_spell[3], lasting_spell[4], lasting_spell[5]-1, lasting_spell[6]]
        
        if cast_spell[5] > 0:
            cast_spells.append(cast_spell)
    
    if boss_hp <= 0:
        global ManaMinimum
        if mana_spent < ManaMinimum:
            ManaMinimum = mana_spent
        return True

    if mana_spent >= ManaMinimum:
        return False
    
    
    if turn == "player":
        for i in range(len(spells)):
            spell = list(spells[i].values())
            spell_is_active = False
            for j in range(len(cast_spells)):
                if cast_spells[j][6] == spell[6]:
                    spell_is_active = True
                    break

            cost = spell[0]
            if cost <= mana and not spell_is_active:
                cast = deepcopy(cast_spells)
                cast.append(spell)
                new_mana_spent = mana_spent + cost
                new_mana = mana - cost
                Battle(boss_hp = boss_hp, hp = hp, mana = new_mana , lasting_spells = cast, turn = "boss", mana_spent = new_mana_spent )
    
    else:
        boss_attack = boss_damage - armor
        if boss_attack < 1:
            boss_attack = 1
        hp -= boss_attack
                
        if hp > 0:
            Battle(boss_hp, hp , mana, cast_spells, "player", mana_spent)

Battle(boss_hp = 51, hp = 50, mana = 500, lasting_spells = [], turn = "player", mana_spent = 0)
print(ManaMinimum)












#%% GOAL 2
"""On the next run through the game, you increase the difficulty to hard.

At the start of each player turn (before any other effects apply), you lose 1 hit point. If this brings you to or below 0 hit points, you lose.

With the same starting stats for you and the boss, what is the least amount of mana you can spend and still win the fight?"""

#%% CALC 2
ManaMinimum = 10000 #just chose a random number sufficiently large

def BattleHard(boss_hp, hp, mana, lasting_spells, turn, mana_spent):
    boss_damage = 9
    armor = 0
    
    if turn == "player":
        hp -= 1
        if hp <= 0:
            return False
    
    #hard_mode        
    cast_spells = []
    for lasting_spell in lasting_spells:
        if lasting_spell[5] >= 0: 
            boss_hp -= lasting_spell[1]
            hp += lasting_spell[2]
            armor += lasting_spell[3]
            mana += lasting_spell[4]

        cast_spell = [lasting_spell[0], lasting_spell[1], lasting_spell[2], lasting_spell[3], lasting_spell[4], lasting_spell[5]-1, lasting_spell[6]]
        
        if cast_spell[5] > 0: # spell carries over
            cast_spells.append(cast_spell)
    
    if boss_hp <= 0:
        global ManaMinimum
        if mana_spent < ManaMinimum:
            ManaMinimum = mana_spent
        return True

    if mana_spent >= ManaMinimum:
        return False
    
    
    if turn == "player":
        for i in range(len(spells)):
            spell = list(spells[i].values())
            spell_is_active = False
            for j in range(len(cast_spells)):
                if cast_spells[j][6] == spell[6]:
                    spell_is_active = True
                    break

            cost = spell[0]
            if cost <= mana and not spell_is_active:
                cast = deepcopy(cast_spells)
                cast.append(spell)
                new_mana_spent = mana_spent + cost
                new_mana = mana - cost
                BattleHard(boss_hp = boss_hp, hp = hp, mana = new_mana , lasting_spells = cast, turn = "boss", mana_spent = new_mana_spent )
    
    else:
        boss_attack = boss_damage - armor
        if boss_attack < 1:
            boss_attack = 1
        hp -= boss_attack
                
        if hp > 0:
            BattleHard(boss_hp, hp , mana, cast_spells, "player", mana_spent)

BattleHard(boss_hp = 51, hp = 50, mana = 500, lasting_spells = [], turn = "player", mana_spent = 0)
print(ManaMinimum)