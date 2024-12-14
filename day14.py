import time
from collections import namedtuple
import re
import sys
from aocd.models import Puzzle
# from rich import print

puzzle = Puzzle(day=14, year=2024)


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


Coord = namedtuple("Coord", ["c", "r"])


def parse(line):
    p, v = line.split(" ")
    return [Coord(*ints(p)), Coord(*ints(v))]


def part_a(input, rs=7, cs=11):
    robots = [parse(line) for line in input.splitlines()]
    for _ in range(100):
        for ro in robots:
            p, v = ro
            ro[0] = (p[0] + v[0]) % cs, (p[1] + v[1]) % rs

    result = None
    for qrt, qrb, qcl, qcr in [
        (0, rs // 2, 0, cs // 2),
        (0, rs // 2, cs // 2 + 1, cs),
        (rs // 2 + 1, rs, 0, cs // 2),
        (rs // 2 + 1, rs, cs // 2 + 1, cs),
    ]:
        quad = 0
        for ro in robots:
            c, r = ro[0]
            if r >= qrt and r < qrb and c >= qcl and c < qcr:
                quad += 1
        if result is None:
            result = quad
        else:
            result *= quad
    return result


def part_b(input, rs=7, cs=11):
    robots = [parse(line) for line in input.splitlines()]
    grid = [[0 for __ in range(cs)] for _ in range(rs)]
    for (c, r), _ in robots:
        grid[r][c] += 1

    for step in range(1000000000):
        for ro in robots:
            p, v = ro
            grid[p[1]][p[0]] -= 1
            p = (p[0] + v[0]) % cs, (p[1] + v[1]) % rs
            grid[p[1]][p[0]] += 1
            ro[0] = p
        consecutive, max_consecutive = 0, 0
        for r in grid:
            for c in r:
                if c > 0:
                    consecutive += 1
                    if consecutive > max_consecutive:
                        max_consecutive = consecutive
                else:
                    consecutive = 0
        if max_consecutive > 7:
            out = [b"\033[2J\033[3J\033[H", str(step + 1).encode()]
            for l in grid:
                out.append(b"".join(b"." if i == 0 else b"#" for i in l))
            sys.stdout.buffer.write(b"\n".join(out))
            sys.stdout.flush()


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = puzzle.examples[0].input_data

check_example(part_a(example), 12)
puzzle.answer_a = part_a(puzzle.input_data, rs=103, cs=101)

# check_example(part_b(example), None)
puzzle.answer_b = part_b(puzzle.input_data, rs=103, cs=101)
