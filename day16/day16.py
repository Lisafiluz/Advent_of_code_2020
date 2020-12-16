def get_file_data(path):
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line.strip() for line in lines]
    return lines_without_spaces

def get_range(file_data):
    index = 0
    while file_data[index] != "":
        range_with_or = file_data[index][file_data[index].index(": ")+2:]
        yield range_with_or.split(" or ")[0]
        yield range_with_or.split(" or ")[1]
        index += 1


def get_range_dict(ranges):
    ranges_dict = {}
    i = 0
    index = 0
    for _ in range(len(ranges) // 2):
        list_v = []
        list_v += range(int(ranges[i].split("-")[0]), int(ranges[i].split("-")[1]) + 1)
        list_v += range(int(ranges[i+1].split("-")[0]), int(ranges[i+1].split("-")[1]) + 1)
        ranges_dict[index] = set(list_v)
        index += 1
        i += 2
    return ranges_dict


def get_seats_by_row(file_data, near_by_ticket_row):
    seats_by_row = {}   
    for seats in file_data[near_by_ticket_row:]:
        index = 0
        for seat in seats.split(","):
            if index in seats_by_row:
                seats_by_row[index].append(int(seat))
            else:   
                seats_by_row[index] = [int(seat)]
            index += 1

    for k, v in seats_by_row.items():
        seats_by_row[k] = set(v)
    return seats_by_row


def get_which_row_to_which_subject_dict(seats_by_row, ranges_dict):
    d = {}
    for k, row in seats_by_row.items():
        for index, subject_row in ranges_dict.items():
            if row.issubset(subject_row):
                if index in d:
                    d[index].add(k)
                else:
                    d[index] = {k}
    numbers_to_remove = set()
    while True:
        flag = True
        for k, v in d.items():
            if len(v) == 1:
                numbers_to_remove.add(next(iter(v)))
            else:
                flag = False
                d[k] = v.difference(numbers_to_remove) 
        if flag:
            break
    return d

if __name__ == "__main__":
    path = "day16/input.txt"
    file_data = get_file_data(path)

    # part 1
    ranges = list(get_range(file_data))
    range_set = set()

    for r in ranges:
        for n in range(int(r.split("-")[0]), int(r.split("-")[1]) + 1):
            range_set.add(n)

    near_by_ticket_row = 25
    invalid_fields = 0
    row_to_discard = 25

    for seats in file_data[near_by_ticket_row:]:
        for seat in seats.split(","):
            if int(seat) not in range_set:
                file_data.pop(row_to_discard)
                row_to_discard -= 1
                invalid_fields += int(seat)
        row_to_discard += 1

    print("part 1: ", invalid_fields)

    # part 2

    ranges_dict = get_range_dict(ranges)
    my_ticket_row = file_data[22].split(',')
    seats_by_row = get_seats_by_row(file_data, near_by_ticket_row)
    which_row_to_which_subject_dict = get_which_row_to_which_subject_dict(seats_by_row, ranges_dict)
    defarture = [next(iter(which_row_to_which_subject_dict[i])) for i in range(6)]
    mul = 1

    for i in defarture:
        mul *= int(my_ticket_row[i])

    print("part 2: ", mul)