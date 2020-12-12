def get_file_data(path):
    # Last line without new line (\n)
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line[0:-1] for line in lines[0:-1]]
    lines_without_spaces.append(lines[-1])
    return lines_without_spaces



def is_need_to_be_occupied(location, current_map):
    COMBINATIONS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
    for x, y in COMBINATIONS:
        try:
            if location[0] + x >= 0 and location[1] + y >= 0:
                if current_map[location[0] + x][location[1] + y] == '#':
                    return False
        except:
            pass
    return True


def is_need_to_be_empty(location, current_map):
    COMBINATIONS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for x, y in COMBINATIONS:
        try:
            if location[0] + x >= 0 and location[1] + y >= 0:
                if current_map[location[0] + x][location[1] + y] == '#':
                    count += 1
        except:
            pass
    
    return count >= 4
        

def is_need_to_be_occupied2(location, current_map):
    COMBINATIONS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
    combination_index = 0
    for x, y in COMBINATIONS:
        try:
            while True:
                if location[0] + x >= 0 and location[1] + y >= 0:
                    if current_map[location[0] + x][location[1] + y] == '#':
                        return False
                    elif current_map[location[0] + x][location[1] + y] == 'L':
                        break
                else:
                    break
                x += COMBINATIONS[combination_index][0]
                y += COMBINATIONS[combination_index][1]
                
        except:
            pass
        combination_index +=1
    return True


def is_need_to_be_empty2(location, current_map):
    COMBINATIONS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
    count = 0
    combination_index = 0
    for x, y in COMBINATIONS:
        try:
            while True:
                if location[0] + x >= 0 and location[1] + y >= 0:
                    if current_map[location[0] + x][location[1] + y] == '#':
                        count += 1
                        break
                    if current_map[location[0] + x][location[1] + y] == 'L':
                        break
                else:
                    break
                x += COMBINATIONS[combination_index][0]
                y += COMBINATIONS[combination_index][1]
        except:
            pass
        combination_index +=1
    return count >= 5


def get_num_of_empty_seats(file_data, is_need_to_be_occupied_func, is_need_to_be_empty_func):
    current_map = file_data
    while True:
        next_map = []
        for row in range(len(current_map)):
            next_map_row = ""
            for seat in range(len(current_map[row])):
                if current_map[row][seat] == '.':
                    next_map_row+='.'
                elif current_map[row][seat] == 'L':
                    if is_need_to_be_occupied_func((row, seat), current_map):
                        next_map_row+='#'
                    else:
                        next_map_row+='L'
                elif current_map[row][seat] =='#':
                    if is_need_to_be_empty_func((row, seat), current_map):
                        next_map_row+='L'
                    else:
                        next_map_row+='#'
            next_map.append(next_map_row)
        if next_map == current_map:
            break
        else:
            current_map = next_map
    counter = 0
    for row in current_map:
        for seat in row:
            if seat == '#':
                counter += 1
    return counter

path = "day11/input.txt"
file_data = get_file_data(path)

# part 1
print(get_num_of_empty_seats(file_data,
                            is_need_to_be_occupied_func=is_need_to_be_occupied,
                            is_need_to_be_empty_func=is_need_to_be_empty))

# part 2
print(get_num_of_empty_seats(file_data,
                            is_need_to_be_occupied_func=is_need_to_be_occupied2,
                            is_need_to_be_empty_func=is_need_to_be_empty2))
