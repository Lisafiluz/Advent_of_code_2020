import collections


def get_file_data(path):
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line.strip() for line in lines]
    return lines_without_spaces


def get_current_degrees(current_degrees, value):
    current_degrees += value
    if current_degrees >= 360:
        current_degrees -= 360
    elif current_degrees < 0:
        current_degrees += 360
    return current_degrees


def part1(rules):
    turns = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    directions = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
    current_direction = 'E'
    current_degrees = 90

    for direction, value in rules:
        if direction == 'F':
            directions[current_direction] += value
        elif direction =='R' or direction =='L':
            value = (value*-1, value) [direction == 'R']
            current_degrees = get_current_degrees(current_degrees, value)
            current_direction = turns[current_degrees]
        else:
            directions[direction] += value
    return abs(directions['S'] - directions['N']) + abs(directions['E'] - directions['W'])


def rotate_way_point(current_way_point, rotates, rotate_dir):
    directions = 'NESW'
    current_way_point_list = [current_way_point[d] for d in directions]
    new_way_point = collections.deque(current_way_point_list)
    new_way_point.rotate(rotate_dir*rotates)
    return {directions[i] : v for i, v in enumerate(new_way_point)}


def part2(rules):
    current_way_point = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
    location = {'N': 0, 'E': 0, 'S': 0, 'W': 0}

    for direction, value in rules:
        if direction == 'F':
            for k, _ in current_way_point.items():
                location[k] += value * current_way_point[k]
        elif direction =='R' or direction == 'L':
            rotate_dir = (-1, 1) [direction == 'R']
            current_way_point = rotate_way_point(current_way_point, rotates=value//90, rotate_dir=rotate_dir)
        else:
            current_way_point[direction] += value
    return abs(location['S'] - location['N']) + abs(location['E'] - location['W'])


path = "day12/input.txt"
file_data = get_file_data(path)
rules = [(l[0], int(l[1:]))for l in file_data]

print(part1(rules))
print(part2(rules))