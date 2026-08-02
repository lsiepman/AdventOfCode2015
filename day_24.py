from itertools import combinations
from math import prod

def solve(packages: list[int], num_groups: int) -> int:
    """
    Finds the minimum Quantum Entanglement for the passenger compartment (Group 1).
    Group 1 must have the fewest packages possible and sum to sum(packages) // num_groups.
    """
    target_weight = sum(packages) // num_groups
    
    # Sort descending to find products or evaluate constraints faster
    packages.sort(reverse=True)
    
    # Search for the smallest possible combination length
    for size in range(1, len(packages) + 1):
        # Generate combinations of the current size only
        valid_combos = [
            combo for combo in combinations(packages, size) 
            if sum(combo) == target_weight
        ]
        
        # If we found valid group(s) of this size, pick the minimum Quantum Entanglement
        if valid_combos:
            return min(prod(combo) for combo in valid_combos)
            
    raise ValueError("No valid grouping found.")

# Read Data
with open("./data/data_24.txt") as file:
    packages = [int(line.strip()) for line in file if line.strip()]

# Solves dynamically for any input dataset
print(f"Part 1: {solve(packages, num_groups=3)}")
print(f"Part 2: {solve(packages, num_groups=4)}")