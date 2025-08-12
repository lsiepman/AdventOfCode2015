# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:39:43 2020

@author: laura
"""

# %% IMPORTS
import operator


# %% FUNCTIONS
def Movement(current_loc, move):
    """Function for tracking locations

    Parameters
    -----------
    current_loc : tuple
        current location coordinate
    move : tuple
        description of movement to new location

    Returns
    -----------
    tuple with new location
    """
    new_loc = tuple(map(operator.add, current_loc, move))

    return new_loc


# %% DATA
data = ""
# %% CALCULATIONS - Part 1
start = (0, 0)
data_split = list(data)

# Converting movement to coordinategrid movements
move_grid = []
for i in data_split:
    if i == "v":
        move_grid.append((0, -1))
    elif i == "<":
        move_grid.append((-1, 0))
    elif i == ">":
        move_grid.append((1, 0))
    else:
        move_grid.append((0, 1))

# Checking all locations
locations = [start]
current_loc = start
for i in move_grid:
    new_loc = Movement(current_loc, i)
    locations.append(new_loc)
    current_loc = new_loc

unique_locations = list(set(locations))

print(len(unique_locations), "houses will receive at least one gift")


# %% CALCULATIONS - Part 2
move_grid_santa = move_grid[0::2]
move_grid_robo = move_grid[1::2]

locations_santa = [start]
current_loc = start
for i in move_grid_santa:
    new_loc = Movement(current_loc, i)
    locations_santa.append(new_loc)
    current_loc = new_loc

locations_robo = [start]
current_loc = start
for i in move_grid_robo:
    new_loc = Movement(current_loc, i)
    locations_robo.append(new_loc)
    current_loc = new_loc

total_locations_year_2 = locations_robo + locations_santa

unique_locations_year_2 = list(set(total_locations_year_2))

print(
    len(unique_locations_year_2),
    "houses will receive at least one gift in the second year",
)
