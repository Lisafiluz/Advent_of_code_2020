def get_file_data(path):
    # Last line without new line (\n)
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line[0:-1] for line in lines[0:-1]]
    lines_without_spaces.append(lines[-1])
    return lines_without_spaces

def is_valid(number, preamble):
    for i in range(len(preamble)):
        j = i + 1
        while j < len(preamble):
            if int(preamble[i]) + int(preamble[j]) == int(number):
                return True
            j += 1
    return False
        

def get_contiguos_range(number, file_data):
    for i in range(len(file_data)):
        j = i + 1
        while j < len(file_data):
            numbers_sum = sum([int(number) for number in file_data[i:j+1]])
            if int(number) == numbers_sum:
                return file_data[i:j+1]
            elif int(number) < numbers_sum:
                break
            j += 1
    return False


if if __name__ == "__main__":
    path = "day9/input.txt"
    file_data = get_file_data(path)

    preamble_length = 25
    preamble = file_data[:preamble_length]
    other_numbers = file_data[preamble_length:]
    weak_num = 0

    for number in other_numbers:
        if not is_valid(number, preamble):
            weak_num = number
            break
        preamble = preamble[1:] + [number]


    contiguous_range = get_contiguos_range(weak_num, file_data)
    contiguous_range_int = [int(number) for number in contiguous_range]
    print(min(contiguous_range_int)+max(contiguous_range_int))