from functools import cache
import inspect
import re
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=19, year=2024)


def dbg(vars):
    frame = inspect.currentframe().f_back
    print(*[f"{var}={frame.f_locals[var]}" for var in vars.split(" ")])


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


@cache
def possible(towels, design):
    if design == "":
        return 1
    matched = 0
    for towel in towels:
        if design.startswith(towel):
            matched += possible(towels, design[len(towel) :])
    return matched


def part_a(input):
    towels, designs = input.split("\n\n")
    towels = towels.split(", ")
    result = 0
    for design in designs.split("\n"):
        if possible(towels, design) > 0:
            result += 1
    return result


def part_b(input):
    towels, designs = input.split("\n\n")
    towels = tuple(towels.split(", "))
    result = 0
    for design in designs.split("\n"):
        result += possible(towels, design)
    return result


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = puzzle.examples[0].input_data

# check_example(part_a(example), 6)
# puzzle.answer_a = part_a(puzzle.input_data)

check_example(part_b(example), 16)
puzzle.answer_b = part_b(puzzle.input_data)
