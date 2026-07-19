
def check_int(value, overview):
    if value.isdigit():
        return int(value)
    else:
        return overview[value]

# PART 1
def executeOperation(row, overview):
    items = row.split(" ")
    
    if "AND" in row:
        val1 = check_int(items[0], overview)
        val2 = check_int(items[2], overview) 
        overview[items[-1]] = val1 & val2
    elif "OR" in row:
        val1 = check_int(items[0], overview)
        val2 = check_int(items[2], overview)
        overview[items[-1]] = val1 | val2
    elif "NOT" in row:
        val1 = overview[items[1]]
        overview[items[-1]] = ~val1
    elif "LSHIFT" in row:
        val1 = check_int(items[0], overview)
        val2 = int(items[2])
        overview[items[-1]] = val1 << val2
    elif "RSHIFT" in row:
        val1 = check_int(items[0], overview)
        val2 = int(items[2])
        overview[items[-1]] = val1 >> val2
    else:
        val1 = check_int(items[0], overview)
        overview[items[-1]] = val1

    return overview

def determineReady(row, overview_keys):
    excludes = ["RSHIFT", "AND", "NOT", "OR", "LSHIFT"]
    relevant = row.split("->")[0].strip()
    items = relevant.split(" ")
    clean = [i for i in items if i not in excludes and not i.isdigit()]
    return set(clean).issubset(overview_keys)

def determineSeen(row, overview_keys):
    result = row.split(" ")[-1]
    return result in overview_keys

def part1(data):
    overview = {}
    seen = set(overview.keys())
    removal = []
    while "a" not in seen:
        data = [i for i in data if i not in removal]
        for i in data:
            if not determineSeen(i, seen) and determineReady(i, seen):
                overview = executeOperation(i, overview)
                seen.update(overview.keys())
                removal.append(i)

    print(f"Part 1 {overview['a']}")
    return overview['a']

def part2(data, start):
    overview = {"b": start}
    seen = set(overview.keys())
    removal = []
    while "a" not in seen:
        data = [i for i in data if i not in removal]
        for i in data:
            if not determineSeen(i, seen) and determineReady(i, seen):
                overview = executeOperation(i, overview)
                seen.update(overview.keys())
                removal.append(i)

    print(f"Part 2 {overview['a']}")


if __name__ == "__main__":

    with open("./data/data_07.txt") as file:
        data = file.read().splitlines()
    new_start = part1(data.copy())
    part2(data, new_start)


