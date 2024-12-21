from functools import cache
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=21, year=2024)


def paths(pad, pos):
    def paths(a, b):
        r, c = pos[a]
        rn, cn = pos[b]
        rs = ("^" if r > rn else "v") * abs(rn - r)
        cs = ("<" if c > cn else ">") * abs(cn - c)
        if c == cn:
            return ["A" + rs + "A"]
        elif r == rn:
            return ["A" + cs + "A"]
        poss = []
        if pad[rn][c] != "#":
            poss.append("A" + rs + cs + "A")
        if pad[r][cn] != "#":
            poss.append("A" + cs + rs + "A")
        return poss

    return paths


numpad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]
numpos = {val: (r, c) for r, row in enumerate(numpad) for c, val in enumerate(row)}
dirpad = [["#", "^", "A"], ["<", "v", ">"]]
dirpos = {val: (r, c) for r, row in enumerate(dirpad) for c, val in enumerate(row)}


def cost(path, depth, pather):
    if depth == 0:
        return len(path) - 1
    return sum(
        min(dircost(subpath, depth - 1) for subpath in pather(s, path[i + 1]))
        for i, s in enumerate(path[:-1])
    )


@cache
def dircost(path, depth):
    return cost(path, depth, paths(dirpad, dirpos))


def solve(input, depth):
    return sum(
        int(code[:-1]) * cost("A" + code, depth + 1, paths(numpad, numpos))
        for code in input.splitlines()
    )


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = """029A
980A
179A
456A
379A"""

check_example(solve(example, 2), 126384)
puzzle.answer_a = solve(puzzle.input_data, 2)
puzzle.answer_b = solve(puzzle.input_data, 25)
