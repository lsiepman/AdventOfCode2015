# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:55:34 2020

@author: laura
"""

# %% GOAL - Part 1
""" They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?"""
# %% IMPORTS
import pandas as pd
import numpy as np

# %% DATA
data = pd.read_csv("Data - Day02.csv", header=None)
# %% CALCULATIONS -Part 1
# getting the data in the right shape
sizes = data[0].str.split("x", expand=True)
sizes = sizes.apply(pd.to_numeric)
sizes = np.array(sizes)
sizes.sort(axis=1)
sizes = pd.DataFrame(sizes)

# area packing paper
sizes["area"] = (
    2 * sizes[0] * sizes[1] + 2 * sizes[0] * sizes[2] + 2 * sizes[1] * sizes[2]
)
sizes["extra"] = sizes[0] * sizes[1]
sizes["total"] = sizes["area"] + sizes["extra"]


print("Wrapping paper needed =", sizes.total.sum(), "sq feet")

# %% GOAL - Part 2
"""Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. """

# %% CALCULATIONS - Part 2
sizes["wrap_ribbon"] = 2 * sizes[0] + 2 * sizes[1]
sizes["bow_ribbon"] = sizes[0] * sizes[1] * sizes[2]
sizes["ribbon_total"] = sizes["wrap_ribbon"] + sizes["bow_ribbon"]

print("Ribbon needed =", sizes.ribbon_total.sum(), "feet")
