def get_file_data(path):
    # Last line without new line (\n)
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
    lines_without_spaces = [line[0:-1] for line in lines[0:-1]]
    lines_without_spaces.append(lines[-1])
    return lines_without_spaces

class CoreInstructor:

    def __init__(self, file_data):
        self.instructions = self.get_instructions(file_data)
        self.acc = 0
        self.index = 0
        self.RULES = {
            "acc": self.plus,
            "nop": self.nothing,
            "jmp": self.jump
        }
        
    def plus(self, value):
        self.index +=1
        self.acc += value
 
    def nothing(self, value):
        self.index += 1
    def jump(self, value):
        self.index += value
    def get_instructions(self, file_data):
        instructions = []
        for line in file_data:
            instructions.append((line.split(' ')[0], int(line.split(' ')[1])))
        return instructions

    def get_acc_until_double_row(self):
        executed_rows = []
        while True:
            if self.index == len(self.instructions):
                return True  # Finished with no double row
            if self.index in executed_rows:
                return self.acc

            executed_rows.append(self.index)
            self.RULES[self.instructions[self.index][0]](self.instructions[self.index][1])

    def get_rows_executing_until_double_row(self):
        self.acc = 0
        executed_rows = []
        self.index = 0
        while True:
            if self.index == len(self.instructions):
                return True  # Finished with no double row
            if self.index in executed_rows:
                return executed_rows

            executed_rows.append(self.index)
            self.RULES[self.instructions[self.index][0]](self.instructions[self.index][1])

    def get_acc_in_the_end(self, instructions):
        self.acc = 0
        executed_rows = []
        self.index = 0
        while True:
            if self.index == len(instructions):
                return self.acc
            if self.index in executed_rows:
                return False

            executed_rows.append(self.index)
            self.RULES[instructions[self.index][0]](instructions[self.index][1])


    def get_new_instructions(self, instructions, switch_i, op):
        new_instructions = []
        for i in range(len(instructions)):
            if i != switch_i:
                new_instructions.append(self.instructions[i])
            else:
                new_instructions.append((op, self.instructions[i][1]))
        return new_instructions

    def get_acc_when_change_row(self):
        for i in range(len(rows_to_check) - 1, 0 , -1):
            if self.instructions[rows_to_check[i]][0] == 'jmp':
                new_instructions = self.get_new_instructions(self.instructions, rows_to_check[i], 'nop')
                is_the_end = self.get_acc_in_the_end(new_instructions)
                if is_the_end:  # got number not false
                    return is_the_end

            elif self.instructions[rows_to_check[i]][0] == 'nop':
                new_instructions = self.get_new_instructions(self.instructions, rows_to_check[i], 'jmp')
                is_the_end = self.get_acc_in_the_end(new_instructions)
                if is_the_end:  # got number not false
                    return is_the_end
        return False


if __name__ == "__main__":
    path = "day8/input.txt"
    file_data = get_file_data(path)

    core = CoreInstructor(file_data)
    print(core.get_acc_until_double_row())
    rows_to_check = core.get_rows_executing_until_double_row()
    print(core.get_acc_when_change_row())