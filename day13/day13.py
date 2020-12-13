import math


def get_file_data(path):
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line.strip() for line in lines]
    return lines_without_spaces


def is_valid(number, bus_ids, to_add):
    for i in range(len(bus_ids)):
        if (number + to_add[i]) % bus_ids[i] != 0:
            return False
    return True


def part1(arrived_in, bus_ids):
    closer_bus = 0
    closer_bus_id = 0
    for bus_id in bus_ids:
        modf, _ = math.modf(arrived_in/bus_id)
        if modf > closer_bus:
            closer_bus = modf
            closer_bus_id = bus_id
    return closer_bus_id * (round(arrived_in/closer_bus_id) * closer_bus_id - arrived_in)


def part2(bus_ids, to_add):
    number = 0
    increament = 1
    index = 1
    count = 0
    previous_number = 0
    while True:
        number += increament
        if is_valid(number, bus_ids[:index], to_add[:index]):
            count += 1
            if count == 1:
                previous_number = number
            else:
                index += 1
                increament = number - previous_number
                count = 0               
            if is_valid(number, bus_ids, to_add):
                return number


path = "day13/input.txt"
file_data = get_file_data(path)

# part1
arrived_in = int(file_data[0])
bus_ids = [int(bus_id) for bus_id in file_data[1].split(',') if bus_id.isdigit()]

print(part1(arrived_in, bus_ids))


# part 2
buses_positions = [bus_id for bus_id in file_data[1].split(',')]
to_add = []
for i in range(len(buses_positions)):
    if buses_positions[i] != 'x':
        to_add.append(i)

print(part2(bus_ids, to_add))