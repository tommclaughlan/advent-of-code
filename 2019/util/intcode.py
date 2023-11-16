
class Intcode:

    def __init__(self, code: list[int]):
        self.code = code
        self.crs = 0
        self.input = 0
        self.output = 0

    def handle_addition(self):
        lhs_pos = self.code[self.crs+1]
        rhs_pos = self.code[self.crs+2]
        res_pos = self.code[self.crs+3]
        lhs = self.code[lhs_pos]
        rhs = self.code[rhs_pos]
        self.code[res_pos] = lhs + rhs
        self.crs += 4

    def handle_multiplication(self):
        lhs_pos = self.code[self.crs+1]
        rhs_pos = self.code[self.crs+2]
        res_pos = self.code[self.crs+3]
        lhs = self.code[lhs_pos]
        rhs = self.code[rhs_pos]
        self.code[res_pos] = lhs * rhs
        self.crs += 4

    def handle_input(self):
        res_pos = self.code[self.crs+1]
        self.code[res_pos] = self.input
        self.crs += 2

    def handle_output(self):
        res_pos = self.code[self.crs+1]
        self.output = self.code[res_pos]
        self.crs += 2

    def modify(self, pos, val):
        self.code[pos] = val

    def load(self, code: list[int]):
        self.code = code

    def run(self):
        self.crs = 0

        while self.code[self.crs] != 99:
            match self.code[self.crs]:
                case 1:
                    self.handle_addition()
                case 2:
                    self.handle_multiplication()
                case 99:
                    break

        return self.code[0]
