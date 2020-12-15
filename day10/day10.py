import itertools


def get_file_data(path):
    # Last line without new line (\n)
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line[0:-1] for line in lines[0:-1]]
    lines_without_spaces.append(lines[-1])
    return lines_without_spaces


def get_adapters_sorted(file_data):
    file_data_numbers = [int(number) for number in file_data]
    return sorted(file_data_numbers)


def part1(file_data):
    one_jolts_differences = 0
    three_jolts_differences = 0
    adapters_sorted = get_adapters_sorted(file_data)
    current_adapter_voltaj = 0
    for adapter in adapters_sorted:
        dif = adapter - current_adapter_voltaj

        if dif == 3:
            three_jolts_differences += 1
        elif dif == 1:
            one_jolts_differences += 1
        
        current_adapter_voltaj = adapter

    three_jolts_differences += 1  # for the finally
    return one_jolts_differences * three_jolts_differences


def is_valid_sequence(sequence):
    for i in range(len(sequence) - 1):
        current = sequence[i]
        next = sequence[i+1]
        if next - current > 3:
            return False
    return True


if __name__ == "__main__":
    path = "day10/input.txt"
    file_data = get_file_data(path)
    # main_sorted_adapters = get_adapters_sorted(file_data)
    print(part1(file_data))

    # part 2
    # The solution:
    # The ordered input contains small sequences for example: 
    # [1, 2, 3, 6, 9, 10, 11] => 1,2,3 | 6 | 9,10,11
    # From each sequence I calculate the possible options to order that sequence and save the first number and the last number
    # In the example above => from 9,10,11 I can get 2 possible orders: 9,10,11 | 9,11
    # Than I multiply the possible options for each sequence and the result is the answer
    # Note that the first sequence starts with 0 because 0 is mandatory