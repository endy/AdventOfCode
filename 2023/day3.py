

import re

schematic = []
numbers = []

with open("day3_problem_input.txt", "r") as input_file:
    row_index = 0
    col_index = 0
    for l in input_file.readlines():
        l = l.strip()
        col_index = 0
        schematic.append(list(l.strip()))
        match = re.search("([0-9]+)", l)

        while match != None:
            num = int(match.group(0))
            index = len(numbers)
            for i in range(col_index + match.span(0)[0], col_index  + match.span(0)[1]):
                schematic[row_index][i] = str(index)
            numbers.append(num)
            col_index += match.span(0)[1]
            match = re.search("([0-9]+)", l[col_index:])

        row_index += 1


search_offsets = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
    ]




def problem1_func(get_gear_ratio):
    sum = 0
    used_nums = []
    gear_ratio_sum = 0
    for r in range(len(schematic)):
        for c in range(len(schematic[r])):
            item = schematic[r][c]
            possible_gear = []
            if item != '.' and item.isdigit() == False:
                for offset in search_offsets:
                    candidate = schematic[r+offset[0]][c+offset[1]]
                    if candidate.isdigit():
                        if candidate not in used_nums:
                            possible_gear.append(numbers[int(candidate)])
                            sum += numbers[int(candidate)]
                            used_nums.append(candidate)
                if get_gear_ratio and len(possible_gear) == 2:
                    ratio = possible_gear[0] * possible_gear[1]
                    gear_ratio_sum += ratio

    if get_gear_ratio:
        return gear_ratio_sum
    else:
        return sum


print(f"Problem 1 sum is {problem1_func(False)}")
print(f"Problem 2 sum is {problem1_func(True)}")