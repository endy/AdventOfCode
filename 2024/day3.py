from collections import defaultdict
import re

day = 3

regex = r"(mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\))"

mul_groups = []
with open(f"day{day}_problem_input.txt", "r") as input_file:
    for l in input_file.readlines():
        mul_groups.extend(re.findall(regex, l))


def part_1():
    product_sum = 0
    for g in mul_groups:
        if g.startswith("do"):
            continue
        x = int(g.split(',')[0].split('(')[-1])
        y = int(g.split(',')[-1].split(')')[0])
        product_sum += x * y
    return product_sum


def part_2():
    product_sum = 0
    do = True
    for g in mul_groups:
        if g.startswith("don't"):
            do = False
        elif g.startswith("do"):
            do = True
        elif do:
            x = int(g.split(',')[0].split('(')[-1])
            y = int(g.split(',')[-1].split(')')[0])
            product_sum += x * y
    return product_sum

problem1 = part_1()
problem2 = part_2()


print(f"Problem 1: {problem1}")
print(f"Problem 2: {problem2}")