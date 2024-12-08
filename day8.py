from collections import defaultdict
from itertools import combinations, product
import re
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=8, year=2024)


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


def part_a(input):
    lines = input.splitlines()
    rs, cs = len(lines), len(lines[0])

    pos = defaultdict(list)
    for r, c in product(range(rs), range(cs)):
        if lines[r][c] != ".":
            pos[lines[r][c]].append((r, c))

    def check(anti):
        return anti[0] >= 0 and anti[0] < rs and anti[1] >= 0 and anti[1] < cs

    results = set()
    for locs in pos.values():
        for a, b in combinations(locs, 2):
            dr, dc = b[0] - a[0], b[1] - a[1]
            aanti = (a[0] - dr, a[1] - dc)
            if check(aanti):
                results.add(aanti)
            banti = (b[0] + dr, b[1] + dc)
            if check(banti):
                results.add(banti)
    return len(results)


def part_b(input):
    lines = input.splitlines()
    rs, cs = len(lines), len(lines[0])

    pos = defaultdict(list)
    for r, c in product(range(rs), range(cs)):
        if lines[r][c] != ".":
            pos[lines[r][c]].append((r, c))

    def check(anti):
        return anti[0] >= 0 and anti[0] < rs and anti[1] >= 0 and anti[1] < cs

    results = set()
    for locs in pos.values():
        for a, b in combinations(locs, 2):
            dr, dc = b[0] - a[0], b[1] - a[1]
            while check(a):
                results.add(a)
                a = (a[0] - dr, a[1] - dc)
            while check(b):
                results.add(b)
                b = (b[0] + dr, b[1] + dc)

    return len(results)


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = puzzle.examples[0].input_data

ex_a = part_a(example)
if ex_a == 0:
    sys.exit(0)
check_example(ex_a, 14)
puzzle.answer_a = part_a(puzzle.input_data)

ex_b = part_b(example)
if ex_b == 0:
    sys.exit(0)
check_example(ex_b, 34)
puzzle.answer_b = part_b(puzzle.input_data)
