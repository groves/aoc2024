from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=1, year=2024)


def part_a(input):
    cs = []
    bs = []
    for line in input.splitlines():
        a, b = [int(x) for x in line.split("   ")]
        cs.append(a)
        bs.append(b)
    cs = sorted(cs)
    bs = sorted(bs)
    sum = 0
    for c, b in zip(cs, bs):
        sum += abs(c - b)
    return sum


def part_b(input):
    cs = []
    bs = []
    for line in input.splitlines():
        a, b = [int(x) for x in line.split("   ")]
        cs.append(a)
        bs.append(b)
    sum = 0
    for c in cs:
        sum += c * bs.count(c)
    return sum


def check_example(solver, input, expected):
    actual = solver(input)
    if isinstance(actual, int):
        actual = str(actual)
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}' with input\n{input}")
        import sys

        sys.exit(1)


for example in puzzle.examples:
    print(example)
    if example.answer_a is not None:
        check_example(part_a, example.input_data, example.answer_a)
    if example.answer_b is not None:
        check_example(part_b, example.input_data, example.answer_b)

puzzle.answer_a = part_a(puzzle.input_data)
puzzle.answer_b = part_b(puzzle.input_data)
