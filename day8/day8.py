def get_file_data(path):
    # Last line without new line (\n)
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line[0:-1] for line in lines[0:-1]]
    lines_without_spaces.append(lines[-1])
    return lines_without_spaces


def get_instructions(file_data):
    instructions = []
    for line in file_data:
        instructions.append((line.split(' ')[0], int(line.split(' ')[1])))
    return instructions


def get_acc(instructions):
    acc = 0
    executed_rows = []
    index = 0
    while True:
        if index == len(instructions):
            return "urike!" + str(acc)
        if index in executed_rows:
            print("acc found", acc)
            return executed_rows

        executed_rows.append(index)
        if instructions[index][0] == 'acc':
            acc += instructions[index][1]
            index += 1
        elif instructions[index][0] == 'nop':
            index += 1
        else:
            index += instructions[index][1]


def get_acc2(instructions):
    acc = 0
    executed_rows = []
    index = 0
    while True:
        if index == len(instructions):
            return True
        if index in executed_rows:
            return False

        executed_rows.append(index)
        if instructions[index][0] == 'acc':
            acc += instructions[index][1]
            index += 1
        elif instructions[index][0] == 'nop':
            index += 1
        else:
            index += instructions[index][1]


def get_new_instructions(instructions, switch_i, op):
    new_instructions = []
    for i in range(len(instructions)):
        if i != switch_i:
            new_instructions.append(instructions[i])
        else:
            new_instructions.append((op, instructions[i][1]))
    return new_instructions


path = "/Users/liluz/Python/Advent_Code_2020/day8/input.txt"
file_data = get_file_data(path)

instructions = get_instructions(file_data)
rows_to_check = get_acc(instructions)

for i in range(len(rows_to_check) - 1, 0 , -1):
    if instructions[rows_to_check[i]][0] == 'jmp':
        new_instructions = get_new_instructions(instructions, rows_to_check[i], 'nop')
        if get_acc2(new_instructions):
            acc = get_acc(new_instructions)
            print(acc)
            break

    elif instructions[rows_to_check[i]][0] == 'nop':
        new_instructions = get_new_instructions(instructions, rows_to_check[i], 'jmp')
        if get_acc2(new_instructions):
            acc = get_acc(new_instructions)
            print(acc)
            break