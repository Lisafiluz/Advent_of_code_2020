def get_file_data(path):
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line.strip() for line in lines]
    return lines_without_spaces


def get_final_number(first_inp, turns):
    game = {}
    # Start of the game
    inp = first_inp.split(',')
    j = 1
    for number in inp:
        game[int(number)] = [j]
        j += 1
    
    # Starting play
    current_number = int(inp[-1])
    for i in range(len(inp) + 1, turns + 1):
        if len(game[current_number]) == 1:
            current_number = 0
            if current_number in game:
                if len(game[0]) == 1:
                    game[current_number].append(i)
                else:
                    game[current_number][0] = game[current_number][1]
                    game[current_number][1] = i
            else:
                game[current_number] = [i]
        else:
            current_number = game[current_number][1] - game[current_number][0]
            if current_number in game:
                if len(game[current_number]) == 1:
                    game[current_number].append(i)
                else:
                    game[current_number][0] = game[current_number][1]
                    game[current_number][1] = i
            else:
                game[current_number] = [i]
    return current_number


path = "day15/input.txt"
file_data = get_file_data(path)

# part 1
print(get_final_number(file_data[0], 2020))

# part 2
print(get_final_number(file_data[0], 30000000))