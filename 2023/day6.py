
day = 6

times = []
distances = []

time_2 = ""
distance_2 = ""

with open(f"day{day}_problem_input.txt", "r") as input_file:


    for t in input_file.readline().split(':')[1].strip().split(' '):
        if t.strip() != '':
            times.append(int(t))
            time_2 += t

    for d in input_file.readline().split(':')[1].strip().split(' '):
        if d.strip() != '':
            distances.append(int(d))
            distance_2 += d


def compute(times, distances):
    result = 1
    for index, t in enumerate(times):
        d = distances[index]
        ways = 0
        for hold_time in range(1, t-1):
            if d < (t - hold_time) * hold_time:
                #print(hold_time)
                ways += 1
        result *= ways

    return result

print(f"Problem 1: {compute(times, distances)}")
print(f"Problem 2: {compute([int(time_2)], [int(distance_2)])}")