def get_file_data(path):
    # Last line without new line (\n)
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line[0:-1] for line in lines[0:-1]]
    lines_without_spaces.append(lines[-1])
    return lines_without_spaces

def get_row_id(end):
    column_max = 127
    column_min = 0
    for i in range(7):
        if end[i] == 'B':
            if column_max - column_min % 2 == 0:
                column_min =  round((column_max + column_min) / 2)
            else:
                column_min =  round((column_max + column_min + 0.5) / 2)
        else:
            if column_max + column_min % 2 == 0:
                column_max = round((column_max + column_min + 0.5) / 2)
            else:
                column_max = round((column_max + column_min - 1) / 2)
    return column_max

def get_column_id(end):
    column_max = 7
    column_min = 0
    for i in range(3):
        if end[i] == 'R':
            if column_max - column_min % 2 == 0:
                column_min =  round((column_max + column_min) / 2)
            else:
                column_min =  round((column_max + column_min + 0.5) / 2)
        else:
            if column_max + column_min % 2 == 0:
                column_max = round((column_max + column_min + 0.5) / 2)
            else:
                column_max = round((column_max + column_min - 1) / 2)
    return column_max



path = "day5/input.txt"
file_data = get_file_data(path)

max_id = 0
set1 = []
for card in file_data:
    seat_id = get_row_id(card[0:7]) * 8 + get_column_id(card[7:])
    set1.append(seat_id)
    if seat_id > max_id:
        max_id = seat_id

set1 = set(set1)
set2 = set([i for i in range(min(set1), max(set1))])
print(set2.difference(set1))