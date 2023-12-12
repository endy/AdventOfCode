day = 11

galaxy_string = ""
galaxy_count = 0
galaxy_coords = []
width =  0
height = 0

with open(f"day{day}_problem_input.txt", "r") as input_file:

    for line in input_file.readlines():
        line = line.strip()
        height += 1
        if width == 0:
            width = len(line)
        galaxy_string += line

def print_galaxy(galaxy_string, w, h):
    for r in range(h):
        l = ""
        for c in range(w):
            index = r * h + c
            l += galaxy_string[index]
        print(f'{r}: {l}')

    print(f"w={width} h={height}")

def empty_cols_rows(width, height):
    global galaxy_string
    global galaxy_count
    global galaxy_coords

    empty_cols = []
    empty_rows = []
    for c in range(0, width):
        empty = True
        for r in range(0, height):
            index = (r * width) + c
            if galaxy_string[index] != '.':
                empty = False
            if galaxy_string[index] == '#':
                # galaxy_string = galaxy_string[:index] + str(galaxy_count) + galaxy_string[index+1:]
                galaxy_count += 1
                galaxy_coords.append((c,r))

        if empty is True:
            empty_cols.append(c)
    for r in range(0, height):
        start = r * width
        end = start + width
        if '#' not in galaxy_string[start:end]:
            empty_rows.append(r)

    return empty_cols, empty_rows

empty_cols, empty_rows = empty_cols_rows(width, height)

pairs = []
for b in range(0, len(galaxy_coords)-1):
    for e in range(b+1, len(galaxy_coords)):
        pairs.append((b, e))

print(f"Total paths: {len(pairs)}")


def problem_func(empty_row_value):
    sum_shortest_length = 0
    for p in pairs:
        b_x = galaxy_coords[p[0]][0]
        b_y = galaxy_coords[p[0]][1]
        e_x = galaxy_coords[p[1]][0]
        e_y = galaxy_coords[p[1]][1]

        dist = abs(e_x - b_x) + abs(e_y - b_y)

        for ec in empty_cols:
            if e_x > b_x:
                if b_x < ec < e_x:
                    dist += empty_row_value
            else:
                if e_x < ec < b_x:
                    dist += empty_row_value

        for er in empty_rows:
            if e_y > b_y:
                if b_y < er < e_y:
                    dist += empty_row_value
            else:
                if e_y < er < b_y:
                    dist += empty_row_value

        sum_shortest_length += dist

    return sum_shortest_length


problem1 = problem_func(1)
problem2 = problem_func(1000000-1)


print(f"Problem 1: {problem1}")
print(f"Problem 2: {problem2}")