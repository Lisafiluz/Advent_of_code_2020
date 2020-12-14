import itertools


def get_file_data(path):
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line.strip() for line in lines]
    return lines_without_spaces


def get_number_after_mask(number, mask):
    number_b_str = str(bin(number))
    result = [m for m in mask]
    mask_index = -1
    for b_digit in number_b_str[-1::-1]:
        if result[mask_index] == 'X':
            result[mask_index] = b_digit
        mask_index -= 1
    after_mask = ""
    for m in result:
        if m == "X" or m =='b':
            after_mask += '0'
        else:
            after_mask += m
    new_number = int(after_mask, 2)
    return new_number


def set_options_to_memory(options_pattern_list, memory, number, combinations):
    X_index = []
    index = 0
    for n in options_pattern_list:
        if n == 'X':
            X_index.append(index)
        index += 1

    index = 0
    for combination in combinations[len(X_index) - 2]:
        for xinedx in X_index:
            options_pattern_list[xinedx] = str(combination[index])
            index += 1
        memory_index = int("".join(options_pattern_list), 2)
        memory[memory_index] = number
        index = 0
    
    return memory


def get_memory_after_mask_row(memory_index, number, mask, memory, combinations):
    number_b_str = str(bin(memory_index))[2:]
    
    result = [m for m in mask]
    mask_index = -1
    for b_digit in number_b_str[-1::-1]:
        if result[mask_index] != 'X':
            if result[mask_index] == '0':
                result[mask_index] = b_digit
        mask_index -= 1
    set_options_to_memory(result, memory, number, combinations)

    return memory


def get_memory_part_2(file_data, combinations):
    memory = {}
    index = 0
    for line in file_data:
        if line[:4] == "mask":
            mask = line[7:]
            index += 1
        else:
            memory = get_memory_after_mask_row(int(line[4:line.index(']')]),
            int(line[line.index("=") + 2:]), mask, memory, combinations)
    return memory



path = "/Users/liluz/Python/Advent_Code_2020/day14/input.txt"
file_data = get_file_data(path)


# part 1
memory = {}
for line in file_data:
    if line[:4] == "mask":
        mask = line[7:]
    else:
        memory[int(line[4:line.index(']')])] = get_number_after_mask(int(line[line.index("=") + 2:]), mask)
print(sum(memory.values()))


# part 2
max_x_appears = 0
for line in file_data:
    if line[:4] == "mask":
        x_appear = 0
        for a in line[7:]:
            if a =='X':
                x_appear += 1
        if x_appear > max_x_appears:
            max_x_appears = x_appear
        x_appear = 0
combinations = []
for i in range(2, max_x_appears + 1):
    combinations.append(list(itertools.product((0,1), repeat=i)))
print(sum(get_memory_part_2(file_data, combinations).values()))