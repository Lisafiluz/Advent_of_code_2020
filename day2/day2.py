def is_valid_password(line):
    presents = line.split(" ")[0]
    min_presents = presents.split('-')[0]
    max_presents = presents.split('-')[1]
    char_to_check = line.split(" ")[1][0]
    password = line.split(" ")[-1]

    if int(min_presents) <= password.count(char_to_check) <= int(max_presents):
        print(min_presents, max_presents, char_to_check, password)
        return True
    return False

def is_valid_password_part2(line):
    indexs = line.split(" ")[0]
    first_index = int(indexs.split('-')[0]) - 1
    second_index = int(indexs.split('-')[1]) - 1
    char_to_check = line.split(" ")[1][0]
    password = line.split(" ")[-1]

    if (password[first_index] == char_to_check and password[second_index] != char_to_check) or (password[first_index] != char_to_check and password[second_index] == char_to_check):
        return True
    return False

with open('/Users/liluz/Python/Advent_Code_2020/day2/input.txt', 'r') as file_handler:
    lines = file_handler.readlines()

valid_passwords = 0
valid_passwords_part2 = 0
for line in lines:
    if is_valid_password(line):
        valid_passwords += 1
    if is_valid_password_part2(line):
        valid_passwords_part2 += 1

print(valid_passwords_part2)
