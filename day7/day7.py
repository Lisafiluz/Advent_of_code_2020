def get_file_data(path):
    # Last line without new line (\n)
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line[0:-1] for line in lines[0:-1]]
    lines_without_spaces.append(lines[-1])
    return lines_without_spaces




path = "/Users/liluz/Python/Advent_Code_2020/day7/input.txt"
file_data = get_file_data(path)
count = 0
sum_bugs = 0
rules = {}
can_hold_my_target = []
search_for = "shiny gold"
for line in file_data:
    sep_line = line.split(" bags contain ")
    rules[sep_line[0]] = sep_line[1]

rules_bags = {}

def get_rules_sorted(rules):
    r = {}
    for main_color, contain_colors in rules.items():
        inner_bugs = []
        sep = contain_colors.split(', ')
        if contain_colors != "no other bags.":
            for s in sep:
                inner_bugs.append({s[s.find(' ') + 1: s.rfind(' ')]:s.split(' ')[0]})
        # else:
        #         inner_bugs.append({s[s.find(' ') + 1: s.rfind(' ')]:0})
        rules_bags[main_color] = inner_bugs
    return rules_bags

rules_sorted = get_rules_sorted(rules)
lll = []
level = 0
def get3(search_for, bags, level):
    if bags == 0:
        return 1
    for c in rules_sorted[search_for]:
        for k,v in c.items():
            lll.append((k, int(v), level + 1))
            
            get3(k, v, level + 1)


def get_whatweget(search_for):
    stack = []
    for  contains in rules_sorted[search_for]:
        while rules_sorted[search_for] != []:
            for k,v in contains.items():
                # if v == nu
                stack.append((int(v), k))
                

#a = get_whatweget(search_for)

get3(search_for, 1, 0)


def get_nodes_lll(lll):
    nodes = {}
    node_to_append = []
    for node in lll:
        if node[2] in nodes:
            nodes[node[2]] += node[1]
        else:
            nodes[node[2]] = node[1]
    return nodes



q = get_nodes_lll(lll)




for main_color, contain_colors in rules.items():
    count_inner_bugs = 0
    sep = contain_colors.split(', ')
    if contain_colors != "no other bags.":
        for s in sep:
            count_inner_bugs += int(s.split(' ')[0])
    rules_bags[main_color] = count_inner_bugs


is_changed = True
def get_can_holds_target(search_for):
    for main_color, contain_colors in rules.items():
        if search_for in contain_colors:
            if main_color not in can_hold_my_target:
                can_hold_my_target.append(main_color)
            get_can_holds_target(main_color)

level = 1
get_can_holds_target(search_for)
print(can_hold_my_target)
def check_with_can_hold(contain_colors):
    for c in can_hold_my_target:
        if c in contain_colors:
            return True
    return False

for main_color, contain_colors in rules.items():
    if search_for in contain_colors or check_with_can_hold(contain_colors):
        count += 1


target = "shiny gold"


print()