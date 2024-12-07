from itertools import product
import re
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=7, year=2024)


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


def calc(input, poss_ops):
    result = 0
    for line in input.splitlines():
        answer, inputs = ints(line)[0], ints(line)[1:]
        for ops in product(poss_ops, repeat=len(inputs) - 1):
            total = inputs[0]
            for input, op in zip(inputs[1:], ops):
                if op == "*":
                    total *= input
                elif op == "|":
                    total = int(str(total) + str(input))
                else:
                    total += input
            if total == answer:
                result += total
                break
    return result


def part_a(input):
    return calc(input, "+*")


def part_b(input):
    return calc(input, "*+|")


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}' with input\n{example}")
        sys.exit(1)


example = puzzle.examples[0].input_data

ex_a = part_a(example)
if ex_a == "":
    sys.exit(0)
check_example(ex_a, 3749)
puzzle.answer_a = part_a(puzzle.input_data)

ex_b = part_b(example)
if ex_b == "":
    sys.exit(0)
check_example(ex_b, 11387)
puzzle.answer_b = part_b(puzzle.input_data)
