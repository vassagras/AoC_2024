import time

class Computer:
    def __init__(self, reg_a, reg_b, reg_c, program):
        self.register_a = reg_a
        self.register_b = reg_b
        self.register_c = reg_c
        self.program =  program
        self.out_list = []
        self.instruction_pointer = 0

    def run_program(self):
        while self.instruction_pointer <= len(self.program) - 2:
            opcode = self.program[self.instruction_pointer]
            operand = self.program[self.instruction_pointer + 1]
            match opcode:
                case 0:
                    self.adv(operand)
                case 1:
                    self.bxl(operand)
                case 2:
                    self.bst(operand)
                case 3:
                    self.jnz(operand)
                case 4:
                    self.bxc()
                case 5:
                    self.out(operand)
                case 6:
                    self.bdv(operand)
                case 7:
                    self.cdv(operand)

    def get_combo_operand(self, operand):
        if operand == 4:
            return self.register_a
        elif operand == 5:
            return self.register_b
        elif operand == 6:
            return self.register_c
        else:
            return operand

    def adv(self, operand):
        self.register_a = int((self.register_a / pow(2,  self.get_combo_operand(operand))))
        self.instruction_pointer += 2

    def bdv(self, operand):
        self.register_b = int((self.register_a / pow(2, self.get_combo_operand(operand))))
        self.instruction_pointer += 2

    def cdv(self, operand):
        self.register_c = int((self.register_a / pow(2,  self.get_combo_operand(operand))))
        self.instruction_pointer += 2

    def bxl(self, operand):
        self.register_b = self.register_b ^ operand
        self.instruction_pointer += 2

    def bst(self, operand):
        self.register_b = self.get_combo_operand(operand) % 8
        self.instruction_pointer += 2

    def bxc(self):
        self.register_b = self.register_b ^ self.register_c
        self.instruction_pointer += 2

    def out(self, operand):
        _ = self.get_combo_operand(operand) % 8
        self.out_list.append(_)
        self.instruction_pointer += 2

    def jnz(self, operand):
        if self.register_a != 0:
            self.instruction_pointer = operand
        else:
            self.instruction_pointer += 2
        return None

    def __str__(self):
        return ",".join([str(i) for i in self.out_list])

start = time.time()
program = [2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]
comp = Computer(47006051, 0, 0, program)
comp.run_program()

end = time.time()
print("Part 1 result: {}".format(comp))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()