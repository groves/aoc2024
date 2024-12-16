from concurrent.futures import ProcessPoolExecutor
import inspect
import re
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=17, year=2024)


def dbg(vars):
    frame = inspect.currentframe().f_back
    print(*[f"{var}={frame.f_locals[var]}" for var in vars.split(" ")])


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


def run(a, b, c, program):
    ip = 0
    outputs = []

    def combo(operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c
            case _:
                raise Exception("You told me this was illegal")

    while ip < len(program):
        operand = program[ip + 1]
        match program[ip]:
            case 0:  # adv
                a //= 2 ** combo(operand)
            case 1:  # bxl
                b ^= operand
            case 2:  # bst
                b = combo(operand) % 8
            case 3:  # jnz
                if a != 0:
                    ip = operand
                    continue
            case 4:  # bxc
                b = b ^ c
            case 5:  # out
                outputs.append(combo(operand) % 8)
            case 6:  # bdv
                b = a // 2 ** combo(operand)
            case 7:  # cdv
                c = a // 2 ** combo(operand)
        ip += 2
    return outputs


# b = a % 8
# b ^= 6
# c = a // 2 ** b
# b ^= c
# b ^= 7
# a // = 2 ** 3
# print b
# a != 0


def part_a(input):
    registers, program = input.split("\n\n")
    a, b, c = ints(registers)
    program = ints(program)
    return ",".join(str(o) for o in run(a, b, c, program))


def part_b(input):
    registers, program = input.split("\n\n")
    a, b, c = ints(registers)
    program = ints(program)
    for a in range(1000000000):
        if program == run(a, b, c, program):
            return a


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = puzzle.examples[0].input_data

# check_example(part_a(example), "4,6,3,5,6,3,5,2,1,0")
# puzzle.answer_a = part_a(puzzle.input_data)

example = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
# check_example(part_b(example), 117440)
step = 100000000
registers, program = puzzle.input_data.split("\n\n")
a, b, c = ints(registers)
program = ints(program)


# while a != 0
# b = a % 8
# b ^= c
# c = a // 2 ** b
# b = b ^ c
# b ^= 7
# a // = 2 ** 3
# output.append(b % 8)

# b = a % 8
# b ^= 6
# c = a // 2 ** b
# b ^= c
# b ^= 7
# a // = 2 ** 3


def get_val(a, b, c):
    b = a % 8
    b ^= 6
    c = a // 2**b
    b ^= c
    b ^= 7
    a //= 2**3
    return b % 8


can = set()
can.add(0)
for num in reversed(program):
    new_can = set()
    for curr in can:
        for k in range(8):
            try_val = (curr << 3) + k
            if get_val(try_val, b, c) == num:
                new_can.add(try_val)
    can = new_can

a = min(can)
print(a)
