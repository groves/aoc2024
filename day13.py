from collections import namedtuple
import re
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=13, year=2024)


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


Button = namedtuple("Button", ["x", "y"])
Machine = namedtuple("Machine", ["a", "b", "x", "y"])


def parse(lines, add=0):
    a = Button(*ints(lines[0]))
    b = Button(*ints(lines[1]))
    x, y = ints(lines[2])
    return Machine(a, b, x + add, y + add)


def check(a, b, x, y, steps=100):
    fewest = None
    for apresses in range(steps + 1):
        ax, ay = a.x * apresses, a.y * apresses
        for bpresses in range(steps + 1):
            bx, by = b.x * bpresses, b.y * bpresses
            curx, cury = ax + bx, ay + by
            if curx > x or cury > y:
                break
            cost = apresses * 3 + bpresses
            if fewest is not None and cost >= fewest:
                break
            if curx == x and cury == y:
                print("Hit", apresses, bpresses, ax, ay, bx, by, x, y)
                if fewest is None or cost < fewest:
                    fewest = cost
                break
    return 0 if fewest is None else fewest


def part_a(input):
    machines = [parse(lines.split("\n")) for lines in input.split("\n\n")]
    return sum(check(*machine) for machine in machines)


def check_cheap(a, b, x, y):
    poss_as = (x * b.y - y * b.x) / (a.x * b.y - a.y * b.x)
    poss_bs = (y * a.x - x * a.y) / (a.x * b.y - a.y * b.x)
    if poss_as == int(poss_as) and poss_bs == int(poss_bs):
        return int(3 * poss_as + poss_bs)
    return 0


def part_b(input):
    machines = [
        parse(lines.split("\n"), add=10000000000000) for lines in input.split("\n\n")
    ]
    return sum(check_cheap(*machine) for machine in machines)


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


for ex in puzzle.examples:
    print(ex.input_data)
example = puzzle.examples[0].input_data

check_example(part_a(example), 480)
puzzle.answer_a = part_a(puzzle.input_data)

check_example(part_b(example), 875318608908)
puzzle.answer_b = part_b(puzzle.input_data)
