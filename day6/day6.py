def get_file_data(path):
    # Last line without new line (\n)
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line[0:-1] for line in lines[0:-1]]
    lines_without_spaces.append(lines[-1])
    return lines_without_spaces



def get_sum_of_group(group_answers_list):
    answers = {}
    for person in group_answers_list:
        for answer in person:
            if answer not in answers:
                answers[answer] = 1
            else:
                answers[answer] += 1
    # return sum
    # part 2 
    all_answers = 0
    for answer, count in answers.items():
        if count == len(group_answers_list):
            all_answers += 1 
    return all_answers


path = "day6/input.txt"
file_data = get_file_data(path)
group = []
sum = 0
for line in file_data:
    if line != "":
        group.append(line)
    else:
        sum += get_sum_of_group(group)
        group = []
sum += get_sum_of_group(group) # for the last group

print(sum)
