
day = 8

import re


with open(f"day8_problem_input.txt", "r") as input_file:

    step_direction_pattern = input_file.readline().strip()
    input_file.readline()

    map = {}

    for line in input_file.readlines():
        groups = re.match("(?P<node>[A-Z0-9]+) = \((?P<L>[A-Z0-9]+), (?P<R>[A-Z0-9]+)\)", line.strip())
        map[groups.group('node')] = {
            'L': groups.group('L'),
            'R': groups.group('R')
            }


def exec_walk(current_nodes, end_in_z):

    walk = True

    steps = 0 
    while walk:
        walk = False
        for node in current_nodes:
            if end_in_z and node[-1] != 'Z':
                walk = True
                break
            elif end_in_z is False and node != 'ZZZ':
                walk = True
                break
        if walk is True:
            direction = steps % len(step_direction_pattern)
            steps += 1
            next_step = step_direction_pattern[direction]
            for i, node in enumerate(current_nodes):
                current_nodes[i] = map[node][next_step]

    return steps


problem1 = exec_walk(['AAA'], False)

starting_nodes = []
for key in map.keys():
    if key[-1] == 'A':
        starting_nodes.append(key)

print(f"Problem 1: {problem1}")

step_list = []
for n in starting_nodes:
    steps = exec_walk([n], True)
    step_list.append(steps)
    print(f"For {n}, take {steps} steps")

import math
# 14893, 20513, 22199, 19951, 17141, 12083

total_steps = math.lcm(*step_list)

problem2 = total_steps

print(f"Problem 2: {problem2}")