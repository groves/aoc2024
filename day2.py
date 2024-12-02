from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=2, year=2024)


def check(vals):
    diffs = []
    for x, y in zip(vals[:-1], vals[1:]):
        diffs.append(x - y)
    return (all(x < 0 for x in diffs) or all(x > 0 for x in diffs)) and all(
        abs(x) > 0 and abs(x) < 4 for x in diffs
    )


def part_a(input):
    safe = 0
    for line in input.splitlines():
        if check([int(x) for x in line.split(" ")]):
            safe += 1

    return safe


def part_b(input):
    safe = 0
    for line in input.splitlines():
        vals = [int(x) for x in line.split(" ")]
        if check(vals):
            safe += 1
            continue
        for i in range(len(vals)):
            sub = vals[:]
            del sub[i]
            if check(sub):
                safe += 1
                break
    return safe


def check_example(solver, input, expected):
    actual = solver(input)
    if isinstance(actual, int):
        actual = str(actual)
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}' with input\n{input}")
        import sys

        sys.exit(1)


for example in puzzle.examples:
    if example.answer_a is not None:
        check_example(part_a, example.input_data, example.answer_a)
    if example.answer_b is not None:
        check_example(part_b, example.input_data, example.answer_b)

puzzle.answer_a = part_a(puzzle.input_data)
puzzle.answer_b = part_b(puzzle.input_data)
