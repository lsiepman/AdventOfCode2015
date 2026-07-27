import pandas as pd

# DATA
time = 2503
with open("./data/data_14.txt") as file:
    data = file.read().splitlines()
  
data = pd.DataFrame(data)
# Part 1
data = data[0].str.split(expand=True)
data = data.drop([1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 14], axis=1)
data.columns = ["Reindeer", "Speed", "Flies", "Rests"]
data[["Speed", "Flies", "Rests"]] = data[["Speed", "Flies", "Rests"]].astype(int)


def DistFly(row, time):
    speed = row["Speed"]
    time_fly = row["Flies"]
    time_rest = row["Rests"]

    distance = 0
    both = time_fly + time_rest

    while time >= both:
        time = time - time_fly - time_rest
        distance = distance + speed * time_fly

    if time >= time_fly:
        time = time - time_fly
        distance = distance + speed * time_fly
    else:
        distance = distance + speed * time

    return distance


distances = []
for i in range(len(data)):
    distances.append(DistFly(data.iloc[i], time))

print(f"Part 1: {max(distances)}")


# Part 2
dist_all = []
for t in range(1, time): # only starts traveling at t=1
    distances = []
    for i in range(len(data)):
        distances.append(DistFly(data.iloc[i], t))
    dist_all.append(distances)

data["Score"] = 0
for i in dist_all:
    max_score = max(i)
    indices = [j for j, x in enumerate(i) if x == max_score]
    for k in indices:
        data.at[k, "Score"] += 1

print(f"Part 2: {max(data["Score"])}")
