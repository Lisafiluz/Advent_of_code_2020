def get_file_data(path):
    # Last line without new line (\n)
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line[0:-1] for line in lines[0:-1]]
    lines_without_spaces.append(lines[-1])
    return lines_without_spaces


def part1(rules):
    turns = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    directions = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
    current_direction = 'E'
    current_degres = 90

    for direction, value in rules:
        if direction == 'F':
            directions[current_direction] += value
        elif direction =='R':
            current_degres += value
            if current_degres >= 360:
                current_degres -= 360
            current_direction = turns[current_degres]    
        elif direction == 'L':
            current_degres -= value
            if current_degres < 0:
                current_degres += 360
            current_direction = turns[current_degres]
        else:
            directions[direction] += value
    return abs(directions['S'] - directions['N']) + abs(directions['E'] - directions['W'])


def rotate_way_point(current_way_point, rotates, rotate_dir):
    new_way_point = {}
    if rotate_dir:  # To the right
        for _ in range(rotates):
            new_way_point['E'] = current_way_point['N']
            new_way_point['S'] = current_way_point['E']
            new_way_point['W'] = current_way_point['S']
            new_way_point['N'] = current_way_point['W']
            current_way_point = new_way_point.copy()


    else:  # To the left
       for _ in range(rotates):
            new_way_point['W'] = current_way_point['N']
            new_way_point['S'] = current_way_point['W']
            new_way_point['E'] = current_way_point['S']
            new_way_point['N'] = current_way_point['E']
            current_way_point = new_way_point.copy()
    return new_way_point


def part2(rules):
    current_way_point = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
    location = {'N': 0, 'E': 0, 'S': 0, 'W': 0}

    for direction, value in rules:
        if direction == 'F':
            for k, _ in current_way_point.items():
                location[k] += value * current_way_point[k]
        elif direction =='R':
            current_way_point = rotate_way_point(current_way_point, value//90, True)
        elif direction == 'L':
            current_way_point = rotate_way_point(current_way_point, value//90, False)
        else:
            current_way_point[direction] += value
    return abs(location['S'] - location['N']) + abs(location['E'] - location['W'])


path = "day12/input.txt"
file_data = get_file_data(path)
rules = [(l[0], int(l[1:]))for l in file_data]

print(part1(rules))
print(part2(rules))


