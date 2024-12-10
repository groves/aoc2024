import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=10, year=2024)


def walk(els: list[list[int]], rs, cs, r, c, walked):
    walked.add((r, c))
    if els[r][c] == 9:
        yield (r, c)
        return

    def check(rn, cn):
        if (
            (rn, cn) in walked
            or rn < 0
            or cn < 0
            or rn == rs
            or cn == cs
            or els[rn][cn] != els[r][c] + 1
        ):
            return
        yield from walk(els, rs, cs, rn, cn, walked)

    yield from check(r + 1, c)
    yield from check(r - 1, c)
    yield from check(r, c + 1)
    yield from check(r, c - 1)


def part_a(input):
    els = [[int(c) for c in line] for line in input.splitlines()]
    rs, cs = len(els), len(els[0])
    result = 0
    for r in range(rs):
        for c in range(cs):
            if els[r][c] == 0:
                result += len(set(walk(els, rs, cs, r, c, set())))
    return result


def paths(els: list[list[int]], rs, cs, r, c):
    for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if rn >= 0 and cn >= 0 and rn < rs and cn < cs and els[rn][cn] == els[r][c] + 1:
            if els[rn][cn] == 9:
                yield 1
            else:
                yield from paths(els, rs, cs, rn, cn)


def part_b(input):
    els = [[int(c) for c in line] for line in input.splitlines()]
    rs, cs = len(els), len(els[0])
    return sum(
        sum(paths(els, rs, cs, r, c))
        for r in range(rs)
        for c in range(cs)
        if els[r][c] == 0
    )


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

check_example(part_a(example), 36)
puzzle.answer_a = part_a(puzzle.input_data)

check_example(part_b(example), 81)
puzzle.answer_b = part_b(puzzle.input_data)
