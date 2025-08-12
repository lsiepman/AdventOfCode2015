# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:02:31 2020

@author: laura

credit to https://www.reddit.com/r/adventofcode/comments/3xspyl/day_22_solutions/cy7mbfz/
"""

# %% IMPORTS
from copy import deepcopy

# %% DATA
missile = {
    "mana": 53,
    "damage": 4,
    "heal": 0,
    "armor": 0,
    "recharge": 0,
    "active": 0,
    "nr": 0,
}
drain = {
    "mana": 73,
    "damage": 2,
    "heal": 2,
    "armor": 0,
    "recharge": 0,
    "active": 0,
    "nr": 1,
}
shield = {
    "mana": 113,
    "damage": 0,
    "heal": 0,
    "armor": 7,
    "recharge": 0,
    "active": 6,
    "nr": 2,
}
poison = {
    "mana": 173,
    "damage": 3,
    "heal": 0,
    "armor": 0,
    "recharge": 0,
    "active": 6,
    "nr": 3,
}
recharge = {
    "mana": 229,
    "damage": 0,
    "heal": 0,
    "armor": 0,
    "recharge": 101,
    "active": 5,
    "nr": 4,
}
spells = [missile, drain, shield, poison, recharge]

# %% SOLUTION 1
ManaMinimum = 10000  # just chose a random number sufficiently large


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

        cast_spell = [
            lasting_spell[0],
            lasting_spell[1],
            lasting_spell[2],
            lasting_spell[3],
            lasting_spell[4],
            lasting_spell[5] - 1,
            lasting_spell[6],
        ]

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
                Battle(
                    boss_hp=boss_hp,
                    hp=hp,
                    mana=new_mana,
                    lasting_spells=cast,
                    turn="boss",
                    mana_spent=new_mana_spent,
                )

    else:
        boss_attack = boss_damage - armor
        if boss_attack < 1:
            boss_attack = 1
        hp -= boss_attack

        if hp > 0:
            Battle(boss_hp, hp, mana, cast_spells, "player", mana_spent)


Battle(boss_hp=51, hp=50, mana=500, lasting_spells=[], turn="player", mana_spent=0)
print(ManaMinimum)


# %% CALC 2
ManaMinimum = 10000  # just chose a random number sufficiently large


def BattleHard(boss_hp, hp, mana, lasting_spells, turn, mana_spent):
    boss_damage = 9
    armor = 0

    if turn == "player":
        hp -= 1
        if hp <= 0:
            return False

    # hard_mode
    cast_spells = []
    for lasting_spell in lasting_spells:
        if lasting_spell[5] >= 0:
            boss_hp -= lasting_spell[1]
            hp += lasting_spell[2]
            armor += lasting_spell[3]
            mana += lasting_spell[4]

        cast_spell = [
            lasting_spell[0],
            lasting_spell[1],
            lasting_spell[2],
            lasting_spell[3],
            lasting_spell[4],
            lasting_spell[5] - 1,
            lasting_spell[6],
        ]

        if cast_spell[5] > 0:  # spell carries over
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
                BattleHard(
                    boss_hp=boss_hp,
                    hp=hp,
                    mana=new_mana,
                    lasting_spells=cast,
                    turn="boss",
                    mana_spent=new_mana_spent,
                )

    else:
        boss_attack = boss_damage - armor
        if boss_attack < 1:
            boss_attack = 1
        hp -= boss_attack

        if hp > 0:
            BattleHard(boss_hp, hp, mana, cast_spells, "player", mana_spent)


BattleHard(boss_hp=51, hp=50, mana=500, lasting_spells=[], turn="player", mana_spent=0)
print(ManaMinimum)
