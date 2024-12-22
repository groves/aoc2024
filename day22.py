from collections import defaultdict
import re
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=22, year=2024)


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


PRUNE = 16777216


def part_a(input):
    result = 0
    for line in input.splitlines():
        secret = int(line)
        for _ in range(2000):
            secret = evolve(secret)
        result += secret
    return result


def evolve(secret):
    secret = (secret ^ (secret * 64)) % PRUNE
    secret = (secret ^ (secret // 32)) % PRUNE
    return (secret ^ (secret * 2048)) % PRUNE


def part_b(input):
    nanners = defaultdict(int)
    for line in input.splitlines():
        secret = int(line)
        p = secret % 10
        seq = (None, None, None, None)
        seen = set()
        for _ in range(2000):
            secret = evolve(secret)
            pn = secret % 10
            seq = (*seq[1:], pn - p)
            p = pn
            if seq[0] is not None and seq not in seen:
                nanners[seq] += pn
                seen.add(seq)
    return max(nanners.values())


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = """1
10
100
2024"""

check_example(part_a(example), 37327623)
puzzle.answer_a = part_a(puzzle.input_data)

exampleb = """1
2
3
2024"""
check_example(part_b(exampleb), 23)
puzzle.answer_b = part_b(puzzle.input_data)
