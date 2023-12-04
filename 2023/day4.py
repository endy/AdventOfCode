

def compute_value(winning_numbers, my_numbers):
    card_value = 0
    for my_num in my_numbers:
        if my_num.strip() == '':
            continue
        if my_num in winning_numbers:
            if card_value == 0:
                card_value = 1
            else:
                card_value *= 2

    return card_value

def count_matching(winning_numbers, my_numbers):
    matches = 0
    for my_num in my_numbers:
        if my_num.strip() == '':
            continue
        if my_num in winning_numbers:
            matches += 1

    return matches

def get_numbers(line):
    tokens = line.strip().split(':')
    tokens = tokens[1].strip().split('|')
    winning_numbers = tokens[0].strip().split(' ')
    my_numbers = tokens[1].strip().split(' ')
    return winning_numbers, my_numbers

total_value = 0
with open(r"E:\Projects\AdventOfCode\2023\day4_problem_input.txt", "r") as input_file:
    for line in input_file.readlines():

        winning_numbers, my_numbers = get_numbers(line)
        computed_value = compute_value(winning_numbers, my_numbers)
        total_value += computed_value

print(f"Problem 1 Total Value: {total_value}")

cards_to_compute = []
with open(r"E:\Projects\AdventOfCode\2023\day4_problem_input.txt", "r") as input_file:

    cards = input_file.readlines()
    cards_to_compute = [i for i in range(len(cards))]
    card_counts = [1 for i in range(len(cards))]

    card_values = [0 for i in range(len(cards))]

    total_value = 0
    while cards_to_compute:
        card_index = cards_to_compute.pop(0)
        winning_numbers, my_numbers = get_numbers(cards[card_index])
        match_count = count_matching(winning_numbers, my_numbers)
        assert card_values[card_index] == 0 or card_values[card_index] == match_count
        card_values[card_index] = match_count
 
    print(card_values)

    for card_index, value in enumerate(card_values):
        inc_count = card_counts[card_index]

        while inc_count > 0:
            for count_index in range(card_index+1, card_index+value+1):
                if count_index < len(card_counts):
                    card_counts[count_index] += 1
                else:
                    break
            inc_count -= 1

    print(card_counts)

    total_cards = 0
    for c in card_counts:
        total_cards += c
    print(len(card_counts))
    print(len(card_values))
    print(len(cards))

    print(f"Problem 2: Total Value {total_cards}")