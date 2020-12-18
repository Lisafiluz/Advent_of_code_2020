import copy
import itertools
import operator

def get_file_data(path):
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line.strip() for line in lines]
    return lines_without_spaces


def get_active_neighbors(layer, r, c, layers_dict_copy, combinations):
    active_neighbors = 0
    for combination in combinations:
        index = tuple(map(operator.add, (layer, r, c), combination))
        if index[0] in layers_dict_copy:
            if 13 > index[1] >= 0 and 13 > index[2] >= 0:
                if index != (layer, r, c):
                    if layers_dict_copy[index[0]][index[1]][index[2]] == '#':
                        active_neighbors += 1
    return active_neighbors
    

if __name__ == "__main__":
    path = "day17/example.txt"
    file_data = get_file_data(path)
    num_of_rox_or_cols = len(file_data) + (2*5)
    # part 1
  
    layers_dict = {i: [['.' for _ in range(num_of_rox_or_cols)] for _ in range(num_of_rox_or_cols)] for i in range(-1*num_of_rox_or_cols, num_of_rox_or_cols, 1)}
           
    row = 5
    for input_r in file_data:
        layers_dict[0][row][5] = input_r[0]
        layers_dict[0][row][6] = input_r[1]
        layers_dict[0][row][7] = input_r[2]
        row += 1
    combinations = list((i, j, k) for k in range(-1, 2, 1) for j in range(-1, 2, 1) for i in range(-1, 2, 1))
    for _ in range(6):
        layers_dict_copy = copy.deepcopy(layers_dict)
        for layer, flat in layers_dict.items():
            for r in range(num_of_rox_or_cols):
                for c in range(num_of_rox_or_cols):
                    active_neighbors = get_active_neighbors(layer, r, c, layers_dict_copy, combinations)
                    
                    if layers_dict[layer][r][c] == '#':
                        if active_neighbors < 2 or active_neighbors > 3:
                            layers_dict[layer][r][c] = '.'
                    else:
                        if active_neighbors == 3:
                            layers_dict[layer][r][c] = '#'
    

    num_of_actives = 0
    for _, flat in layers_dict.items():
        for r in flat:
            for c in r:
                if c == "#":
                    num_of_actives += 1
    print(num_of_actives)
  

    # part 2

    