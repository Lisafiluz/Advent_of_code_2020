def get_pasports(path):
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines[1068]
    lines_without_spaces = [line[0:-1] for line in lines]
    
    passport_list = []
    current_passport = []
    for line in lines_without_spaces:
        if line != "":
            current_passport += line.split(" ")
        else:
            passport_list.append(current_passport)
            current_passport = []
        
    passport_list.append(current_passport)

    dict_passports = []
    for human in passport_list:
        d = {}
        for detail in human:
            key = detail.split(':')[0]
            value = detail.split(':')[1]
            d[key] = value
        dict_passports.append(d)
    
    return dict_passports 

def check_letters(string):
    legal_chars = ['a', 'b','c', 'd','e', 'f','0', '1','2', '3','4', '5','6', '7','8', '9']
    for c in string:
        if c not in legal_chars:
            return True
    return False


def is_valid(human):
    if int(human['byr']) > 2002 or int(human['byr']) < 1920:
        return False
    if int(human['iyr']) > 2020 or int(human['iyr']) < 2010:
        return False
    if int(human['eyr']) > 2030 or int(human['eyr']) < 2020:
        return False
    if "cm" not in human['hgt'] and "in" not in human['hgt']:
        return False
    elif human['hgt'][-2:] == "cm":
        if int(human['hgt'][:-2]) < 150 or int(human['hgt'][:-2]) > 193:
            return False
    elif human['hgt'][-2:] == "in":
        if int(human['hgt'][:-2]) < 59 or int(human['hgt'][:-2]) > 76:
            return False
    if human['hcl'][0] != '#' or len(human['hcl']) != 7 or check_letters(human['hcl'][1:]):
        return False
    if human['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if len(human['pid']) != 9:
        return False
    return True


def get_valid_passports(passports):
    count = 0
    for human in passports:
        if len(human) == 8:
            if is_valid(human):
                count += 1
        elif len(human) == 7 and "cid" not in human.keys():
            if is_valid(human):
                count += 1
    return count


path = "day4/input.txt"

passports = get_pasports(path)
valid = get_valid_passports(passports)
print(valid)

