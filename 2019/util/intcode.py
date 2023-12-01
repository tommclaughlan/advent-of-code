
class Intcode:

    def __init__(self, code: list[int]):
        self.code = code
        self.crs = 0
        self.input = 0
        self.output = 0
        self.opcode = 0
        self.mode = '000'
        self.should_return_output = False

    def parse_mode(self, mode):
        mode_as_string = str(mode).zfill(5)
        return int(mode_as_string[-2:]), mode_as_string[0:3]

    def parse_io_parameters(self):
        pos = self.crs + 1

        return self.code[pos] if self.mode[2] == '0' else pos

    def parse_jmp_parameters(self):
        tst_pos = self.code[self.crs + 1]
        jmp_pos = self.code[self.crs + 2]
        tst = self.code[tst_pos] if self.mode[2] == '0' else tst_pos
        jmp = self.code[jmp_pos] if self.mode[1] == '0' else jmp_pos
        return tst, jmp

    def parse_op_parameters(self):
        lhs_pos = self.code[self.crs + 1]
        rhs_pos = self.code[self.crs + 2]
        res_pos = self.crs + 3
        lhs = self.code[lhs_pos] if self.mode[2] == '0' else lhs_pos
        rhs = self.code[rhs_pos] if self.mode[1] == '0' else rhs_pos
        out_pos = self.code[res_pos] if self.mode[0] == '0' else res_pos
        return lhs, rhs, out_pos

    def handle_addition(self):
        lhs, rhs, res = self.parse_op_parameters()

        result = lhs + rhs
        self.code[res] = result
        self.crs += 4

    def handle_multiplication(self):
        lhs, rhs, res = self.parse_op_parameters()

        result = lhs * rhs
        self.code[res] = result
        self.crs += 4

    def handle_input(self):
        res_pos = self.parse_io_parameters()
        self.code[res_pos] = self.input
        self.crs += 2

    def handle_output(self):
        res_pos = self.parse_io_parameters()
        out = self.code[res_pos]
        self.output = out
        if self.output != 0:
            print("error")
        self.crs += 2

    def handle_jump_if_true(self):
        tst, jmp = self.parse_jmp_parameters()
        if tst != 0:
            self.crs = jmp
        else:
            self.crs += 3

    def handle_jump_if_false(self):
        tst, jmp = self.parse_jmp_parameters()
        if tst == 0:
            self.crs = jmp
        else:
            self.crs += 3

    def handle_less_than(self):
        lhs, rhs, pos = self.parse_op_parameters()
        if lhs < rhs:
            self.code[pos] = 1
        else:
            self.code[pos] = 0
        self.crs += 4

    def handle_equals(self):
        lhs, rhs, pos = self.parse_op_parameters()
        if lhs == rhs:
            self.code[pos] = 1
        else:
            self.code[pos] = 0
        self.crs += 4

    def modify(self, pos, val):
        self.code[pos] = val

    def load(self, code: list[int]):
        self.code = code

    def return_output(self):
        self.should_return_output = True

    def run(self):
        self.crs = 0

        while self.code[self.crs] != 99:
            self.opcode, self.mode = self.parse_mode(self.code[self.crs])
            match self.opcode:
                case 1:
                    self.handle_addition()
                case 2:
                    self.handle_multiplication()
                case 3:
                    self.handle_input()
                case 4:
                    self.handle_output()
                case 5:
                    self.handle_jump_if_true()
                case 6:
                    self.handle_jump_if_false()
                case 7:
                    self.handle_less_than()
                case 8:
                    self.handle_equals()
                case 99:
                    break

        if self.should_return_output:
            return self.output
        else:
            return self.code[0]
