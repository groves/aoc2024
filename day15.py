import inspect
import re
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=15, year=2024)


def d(*varlines):
    frame = inspect.currentframe().f_back
    for vars in varlines:
        print(*[f"{var}={frame.f_locals[var]}" for var in vars.split(" ")])


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


dirs = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}


def part_a(input):
    map, moves = input.split("\n\n")
    map = [list(s) for s in map.split("\n")]
    moves = moves.replace("\n", "")
    rs, cs = len(map), len(map[0])
    rr, rc = 0, 0
    for r in range(rs):
        for c in range(cs):
            if map[r][c] == "@":
                rr, rc = (r, c)
                break
    for move in moves:
        h, v = dirs[move]
        rn, cn = rr, rc
        while (cur := map[rn][cn]) != "#" and cur != ".":
            rn, cn = rn + v, cn + h
        if cur == "#":
            continue
        rr, rc = rn, cn
        while True:
            rn, cn = rn - v, cn - h
            cur = map[rn][cn]
            map[rr][rc] = cur
            if cur == "@":
                break
            rr, rc = rn, cn
        map[rn][cn] = "."
    result = 0
    for r in range(rs):
        for c in range(cs):
            if map[r][c] == "O":
                result += 100 * r + c
    return result


def h_move(rr, rc, map, h):
    rn, cn = rr, rc
    while (cur := map[rn][cn]) != "#" and cur != ".":
        rn, cn = rn, cn + h
    if cur == "#":
        return rr, rc
    rr, rc = rn, cn
    while True:
        rn, cn = rn, cn - h
        cur = map[rn][cn]
        map[rr][rc] = cur
        if cur == "@":
            break
        rr, rc = rn, cn
    map[rn][cn] = "."
    return rr, rc


def v_move(rr, rc, map, v):
    rn = rr
    acs = [{rc}]
    while True:
        rn += v
        acn = set()
        for c in acs[-1]:
            if map[rn][c] == "]":
                acn.update([c - 1, c])
            elif map[rn][c] == "[":
                acn.update([c, c + 1])
            elif map[rn][c] == "#":
                return rr, rc
        if len(acn) == 0:
            break
        acs.append(acn)
    for ac in reversed(acs):
        rp = rn
        rn -= v
        for c in ac:
            map[rp][c] = map[rn][c]
            map[rn][c] = "."
    return rp, rc


def part_b(input):
    mapi, moves = input.split("\n\n")

    map = []
    for line in mapi.split("\n"):
        r = []
        for c in line:
            if c == "#":
                r.extend("##")
            elif c == "O":
                r.extend("[]")
            elif c == ".":
                r.extend("..")
            else:
                r.extend("@.")
        map.append(r)
    moves = moves.replace("\n", "")
    rs, cs = len(map), len(map[0])
    rr, rc = 0, 0
    for r in range(rs):
        for c in range(cs):
            if map[r][c] == "@":
                rr, rc = (r, c)
                break
    for move in moves:
        h, v = dirs[move]
        if h != 0:
            rr, rc = h_move(rr, rc, map, h)
        else:
            rr, rc = v_move(rr, rc, map, v)
    result = 0
    for r in range(rs):
        for c in range(cs):
            if map[r][c] == "[":
                result += 100 * r + c
    return result


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


ex1 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
ex1a = 2028


ex2 = puzzle.examples[0].input_data
ex2a = 10092

for ex, a in [(ex1, ex1a), (ex2, ex2a)]:
    check_example(part_a(ex), a)
puzzle.answer_a = part_a(puzzle.input_data)

ex3 = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""
# part_b(ex3)
check_example(part_b(ex2), 9021)
puzzle.answer_b = part_b(puzzle.input_data)
