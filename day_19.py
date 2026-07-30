import re

# DATA
replacements = []
with open("./data/data_19.txt") as file:
    for line in file:
        if "=>" in line:
            line_list = re.split(r'\W', line)
            fro = line_list[0]
            to = line_list[-2]
            replacements.append((fro, to))
        elif len(line) < 2:
            pass
        else:
            molecule = line.strip()

# Part 1      
distinct_molecules = set()
for fro, to in replacements:
    for idx in range(len(molecule)):
        # check if the current replacement can be applied
        if molecule[idx:idx+len(fro)] == fro:
            # replace and add to possible resulting molecules
            new_molecule = molecule[:idx] + to + molecule[idx+len(fro):]
            distinct_molecules.add(new_molecule)
print(f"Part 1: {len(distinct_molecules)}")


# # Part 2
def replace_section(molecule, replacements):
    """Replaces molecule based on replacements. Replaced from 'right to left', 
    so opposite from part 1.

    Args:
        molecule (str): starting molecule

    Yields:
        string: new molecule after replacement has been done
    """
    for to, fro in replacements:
        for idx in range(len(molecule)):
            if molecule[idx:idx+len(fro)] == fro:
                new_molecule = molecule[:idx] + to + molecule[idx+len(fro):]
                yield new_molecule

# sort replacements so longest replacements go first
replacements = sorted(replacements, key=lambda x: -len(x[1]))

visited = {molecule}
molecule_list = [molecule]

steps = 0
while True:
    temp_molecule_list = []
    for i in molecule_list:
        for j in replace_section(i, replacements):
            if j in visited:
                continue
            temp_molecule_list.append(j)
            visited.add(j)
            break # only perform the largest replacement (based on order)
    molecule_list = temp_molecule_list
    steps += 1
    if molecule_list[0] == 'e': # ending molecule
        print(f"Part 2: {steps}")
        break
    
