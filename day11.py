import re
import sys
from aocd.models import Puzzle
from rich import print
from functools import lru_cache

puzzle = Puzzle(day=11, year=2024)


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


@lru_cache(None)
def expand(s, times):
    if times == 0:
        return 1
    t1 = times - 1
    if s == 0:
        return expand(1, t1)
    else:
        strstone = str(s)
        if len(strstone) % 2 == 1:
            return expand(s * 2024, t1)
        else:
            return expand(int(strstone[: len(strstone) // 2]), t1) + expand(
                int(strstone[len(strstone) // 2 :]), t1
            )


def blink(input, times):
    return sum(expand(s, times) for s in ints(input))


def part_a(input):
    return blink(input, 25)


def part_b(input):
    return blink(input, 75)


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = "125 17"

check_example(part_a(example), 55312)
puzzle.answer_a = part_a(puzzle.input_data)

puzzle.answer_b = part_b(puzzle.input_data)
