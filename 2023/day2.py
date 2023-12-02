


test_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def get_rgb_count(samples: str):

    r = 0
    g = 0
    b = 0

    for index, sample in enumerate(samples.split(';')):
        for cube_str in sample.strip().split(','):
            cube_tokens = cube_str.strip().split(' ')
            color = cube_tokens[1]
            count = int(cube_tokens[0])
            if color == "red":
                r =  max(r, count)
            elif color == "green":
                g = max(g, count)
            elif color == "blue":
                b = max(b, count)

    return (r, g, b)


def detect_possible(input, r_count, g_count, b_count):

    game_str, samples = input.strip().split(':')
    game = int(game_str.split(' ')[1])

    r_max, g_max, b_max = get_rgb_count(samples)

    possible_id = 0

    if r_max > r_count or g_max > g_count or b_max > b_count:
        pass
        #print(f"Game {game} is not possible")
    else:
        possible_id = int(game)


    return possible_id


def power_of_fewest_possible(input):
    game_str, samples = input.strip().split(':')
    game = int(game_str.split(' ')[1])

    r_max, g_max, b_max = get_rgb_count(samples)

    return r_max * g_max * b_max


id_sum =  0
power_sum = 0
for line in test_input.splitlines():
    if line.strip() != "":
        id_sum += detect_possible(line, 12, 13, 14)
        power_sum += power_of_fewest_possible(line)

print(f"Possible Game Id Sum: {id_sum}")
print(f"Problem 2 - Power Sum: {power_sum}")

id_sum = 0
power_sum = 0
with open("day2_problem_input.txt", "r") as input_file:
    for line in input_file.readlines():
        if line.strip() != "":
            id_sum += detect_possible(line, 12, 13, 14)
            power_sum += power_of_fewest_possible(line)

print(f"Problem 1 - Possible Game Id Sum: {id_sum}")
print(f"Problem 2 - Power Sum: {power_sum}")