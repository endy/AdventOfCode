day = 1


import re

a = []
b = []

from collections import defaultdict
a_count = defaultdict(int)
b_count = defaultdict(int)
with open(f"day{day}_problem_input.txt", "r") as input_file:
    for line in input_file.readlines():
        groups = re.findall("([0-9]+)", line)
        a.append(groups[0])
        a_count[groups[0]] += 1

        b.append(groups[1])
        b_count[groups[1]] += 1

a = sorted(a)
b = sorted(b)



def part_1():
    dist = 0
    for p0, p1 in zip(a, b):
        dist += abs(int(p0) - int(p1))

    return dist

def part_2():
    sim_score = 0
    for key, _ in a_count.items():
        if key in b_count.keys():
            sim_score += b_count[key] * int(key)
    return sim_score


problem1 = part_1()
problem2 = part_2()


print(f"Problem 1: {problem1}")
print(f"Problem 2: {problem2}")