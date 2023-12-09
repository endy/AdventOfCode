
day = 9

sequence_list = []

with open(f"day{day}_problem_input.txt", "r") as input_file:
    for line in input_file.readlines():
        seq = []
        for value in line.strip().split(' '):
            seq.append(int(value))
        sequence_list.append(seq)


def compute_differences(seq: list):

    diff_list = []
    prev_value = seq[0]
    all_zeros = True
    for value in seq[1:]:
        next_value = value-prev_value
        if next_value != 0:
            all_zeros = False
        diff_list.append(next_value)
        prev_value = value

    return all_zeros, diff_list


def get_next_value(seq: list):
    next_value = seq[-1]
    
    finished = False
    next_seq = seq
    while not finished:
        finished, next_seq = compute_differences(next_seq)
        next_value += next_seq[-1]

    return next_value


def problem1_func():
    next_value_sum = 0
    for seq in sequence_list:
        next_value = get_next_value(seq)
        next_value_sum += next_value
    return next_value_sum

problem1 = problem1_func()



def get_new_first_value(seq: list):

    reverse_seq_list = [seq]

    finished = False
    next_seq = seq
    while not finished:
        finished, next_seq = compute_differences(next_seq)
        reverse_seq_list.append(next_seq)

    reverse_seq_list.reverse()

    new_first_value = 0
    for seq in reverse_seq_list[1:]:
        new_first_value = seq[0] - new_first_value

    return new_first_value

def problem2_func():
    first_value_sum = 0
    for seq in sequence_list:
        first_new_value = get_new_first_value(seq)
        first_value_sum += first_new_value
    return first_value_sum


problem2 = problem2_func()


print(f"Problem 1: {problem1}")
print(f"Problem 2: {problem2}")