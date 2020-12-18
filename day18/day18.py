def get_file_data(path):
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line.strip() for line in lines]
    return lines_without_spaces


def get_result(first_num, op, second_num):
    return int(first_num) * int(second_num) if op == '*' else int(first_num) + int(second_num)


def get_expression(line, plus_before_multi):
    first_num = None
    ex = []
    line_list = line.split(' ')
    for num_or_op in line_list:
        if "(" in num_or_op:
            if len(ex) > 0:  # For isolatolating only the inner parentheses
                ex = []
                ex.append(num_or_op[num_or_op.rindex('(') + 1:])
            else:
                ex.append(num_or_op[num_or_op.rindex('(') + 1:])
            first_num = num_or_op[num_or_op.rindex('(') + 1:]
        elif ")" in num_or_op:
            ex.append(num_or_op[:num_or_op.index(')')])
            if len(ex) > 3:  # We got expression that includes more then one expressions inside
                r = get_expression(" ".join(ex), plus_before_multi)
                return (line.replace(" ".join(ex), r[0], 1),
                        r[1])
            second_num = num_or_op[:num_or_op.index(')')]
            result = get_result(first_num, op, second_num)
            return (line.replace("(" + first_num + " " + op + " " + second_num + ")",
                                str(result), 1),
                    result)
        else:
            if len(ex) > 0:
                ex.append(num_or_op)
            op = num_or_op
    if not first_num:  # The expression doesn't contain '('
        if plus_before_multi:
            index = 0
            for num_or_op in line_list:
                if num_or_op == '+':
                    result = get_result(line_list[index-1], num_or_op, line_list[index+1])
                    return (line.replace(line_list[index-1] + " " + num_or_op + " " + line_list[index+1], str(result), 1),
                            result)
                index += 1 
        first_num = line_list[0]
        op = line_list[1]
        second_num = line_list[2]
        result = get_result(first_num, op, second_num)
        return (line.replace(first_num + " " + op + " " + second_num, str(result), 1),
                result)


def get_resut_of_line(line, plus_before_multi):
    while True:
        line, result = get_expression(line, plus_before_multi)
        if line.find(" ") == -1:  # The result of the line is found, for ex: line =  "237", result = 237
            return result


if __name__ == "__main__":
    path = "day18/input.txt"
    file_data = get_file_data(path)

    # part 1
    all_results = 0
    for line in file_data:
        all_results += get_resut_of_line(line, plus_before_multi=False)
    print("Part1: ", all_results)        
            
    # part 2
    all_results = 0
    for line in file_data:
        all_results += get_resut_of_line(line, plus_before_multi=True)
    print("Part2: ", all_results)  