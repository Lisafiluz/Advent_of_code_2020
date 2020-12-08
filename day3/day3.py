def get_map(path):
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()

    lines_without_spaces = [line[0:-1] for line in lines[0:-1]]
    lines_without_spaces.append(lines[-1])
    return [line*100 for line in lines_without_spaces]


def get_encounter_trees(map, steps_right, steps_below):
    current_row = 0
    current_position = 0
    trees = 0
    while current_row < len(map) - 1:
        current_position += steps_right
        current_row += steps_below

        if map[current_row][current_position] == "#":
            trees += 1
    return trees


path = "/Users/liluz/Python/Advent_Code_2020/day3/input.txt"
map = get_map(path)
trees1 = get_encounter_trees(map, 1, 1)
trees2 = get_encounter_trees(map, 3, 1)
trees3 = get_encounter_trees(map, 5, 1)
trees4 = get_encounter_trees(map, 7, 1)
trees5 = get_encounter_trees(map, 1, 2)
print(trees1 * trees2 * trees3 * trees4 * trees5)
