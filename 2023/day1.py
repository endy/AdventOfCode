
"""
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

numbers_reversed = [i[::-1] for i in numbers]

def get_index_for_number(entry: str):
    zero_ascii_value = ord("0")

    for i, c in enumerate(entry):
        if 0 <= ord(c) - zero_ascii_value <= 9:
            return i
    return -1

def get_index_for_string_number(entry: str, string_numbers: list[str]):
    
    index = len(entry)
    number = 0

    import re
    for s in string_numbers:
        m = re.search(s, entry)
        if m is not None:
            if m.span(0)[0] < index:
                index = m.span(0)[0]
                number = string_numbers.index(entry[m.span(0)[0]:m.span(0)[1]])

    if index == len(entry):
        index = -1

    return index, number


def gen_number_from_input(entry):
    first_num_index = get_index_for_number(entry)
    last_num_index = len(entry) - get_index_for_number(reversed(entry)) - 1
    value = int(entry[last_num_index]) + int(entry[first_num_index]) * 10
    return value


def gen_number_from_input_2(entry):
    first_num_index = get_index_for_number(entry)

    last_num_index = get_index_for_number(reversed(entry))
    if last_num_index != -1:
        last_num_index = len(entry) - last_num_index  - 1

    first_str_num_index, first_num_str_value = get_index_for_string_number(entry, numbers)
    last_str_num_index, last_num_str_value = get_index_for_string_number(entry[::-1], numbers_reversed)

    if last_str_num_index != -1:
        last_str_num_index = len(entry) - last_str_num_index - 1

    number = 0

    if first_num_index >= 0 and first_str_num_index >= 0:
        if first_num_index < first_str_num_index:
            number += int(entry[first_num_index]) * 10
        else:
            number += first_num_str_value * 10
    elif first_num_index >= 0:
        number += int(entry[first_num_index]) * 10
    elif first_str_num_index >= 0:
        number += first_num_str_value * 10

    if last_num_index >= 0 and last_str_num_index >= 0:
        if last_num_index > last_str_num_index:
            number += int(entry[last_num_index])
        else:
            number += last_num_str_value
    elif last_num_index >= 0:
        number += int(entry[last_num_index])
    elif last_str_num_index >= 0:
        number += last_num_str_value

    print(f"{number} {entry.strip()}")

    return number


sum = 0
sum2 = 0
with open("day1_problem_input.txt", "r") as input_text_file:
    for line in input_text_file.readlines():
        sum += gen_number_from_input(line)
        sum2 += gen_number_from_input_2(line)
print(f"Problem 1 answer is {sum}")
print(f"Problem 2 answer is {sum2}")


