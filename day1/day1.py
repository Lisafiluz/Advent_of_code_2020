def get_file_data(path):
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [int(line.strip()) for line in lines]
    return lines_without_spaces


path = "day1/input.txt"
file_data = get_file_data(path)

for index in range(0, len(file_data) - 2):
    num1 = file_data[index]
    index2 = index + 1
    for index2 in range(index + 1, len(file_data) - 1):
        num2 = file_data[index2]
        index3 = index2 + 1
        for index3 in range(index2 + 1, len(file_data)):
            num3 = file_data[index3]
            if num1 + num2 + num3 == 2020:
                print(num1, num2, num3, num1*num2*num3)