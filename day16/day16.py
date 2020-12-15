def get_file_data(path):
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line.strip() for line in lines]
    return lines_without_spaces


if __name__ == "__main__":
    path = "day15/input.txt"
    file_data = get_file_data(path)

    # part 1

    # part 2
