import sys
from aocd.models import Puzzle
from rich import print as rprint

puzzle = Puzzle(day=6, year=2024)


def part_a(input):
    rows = []
    r, c = 0, 0
    for line in input.splitlines():
        if "^" in line:
            r, c = len(rows), line.index("^")
        rows.append([c == "#" for c in line])
    visited = set([(r, c)])
    dr, dc = -1, 0
    while r + dr >= 0 and r + dr < len(rows) and c + dc >= 0 and c + dc < len(rows[0]):
        while rows[r + dr][c + dc]:
            if dr == -1:
                dc = 1
                dr = 0
            elif dr == 1:
                dr = 0
                dc = -1
            elif dc == 1:
                dc = 0
                dr = 1
            else:
                dc = 0
                dr = -1
            if (
                r + dr < 0
                or r + dr == len(rows)
                or c + dc < 0
                or c + dc == len(rows[0])
            ):
                return len(visited)
        r += dr
        c += dc
        visited.add((r, c))
        if False:
            for tr, row in enumerate(rows):
                for tc, col in enumerate(row):
                    if tr == r and tc == c:
                        print("^", end="")
                    elif (tr, tc) in visited:
                        print("X", end="")
                    elif col:
                        print("#", end="")
                    else:
                        print(".", end="")
                print()
            print(dr, dc)
            print()
    return len(visited)


def check_loop(r: int, c: int, rows):
    dr, dc = -1, 0
    visited = set([(r, c, dr, dc)])
    while r + dr >= 0 and r + dr < len(rows) and c + dc >= 0 and c + dc < len(rows[0]):
        while rows[r + dr][c + dc]:
            if dr == -1:
                dc = 1
                dr = 0
            elif dr == 1:
                dr = 0
                dc = -1
            elif dc == 1:
                dc = 0
                dr = 1
            else:
                dc = 0
                dr = -1
            if (
                r + dr < 0
                or r + dr == len(rows)
                or c + dc < 0
                or c + dc == len(rows[0])
            ):
                return False
        r += dr
        c += dc
        if (r, c, dr, dc) in visited:
            return True
        visited.add((r, c, dr, dc))
        if False:
            for tr, row in enumerate(rows):
                for tc, col in enumerate(row):
                    if tr == r and tc == c:
                        print("^", end="")
                    elif (tr, tc) in visited:
                        print("X", end="")
                    elif col:
                        print("#", end="")
                    else:
                        print(".", end="")
                print()
            print(dr, dc)
            print()
    return False


def part_b(input):
    rows = []
    r, c = 0, 0
    for line in input.splitlines():
        if "^" in line:
            r, c = len(rows), line.index("^")
        rows.append([c == "#" for c in line])

    loops = 0
    for obr in range(len(rows)):
        for obc in range(len(rows[0])):
            if rows[obr][obc] or (obr, obc) == (r, c):
                continue
            rows[obr][obc] = True
            if check_loop(r, c, rows):
                loops += 1
            rows[obr][obc] = False
    return loops


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = puzzle.examples[0].input_data

ex_a = part_a(example)
check_example(ex_a, 41)
puzzle.answer_a = part_a(puzzle.input_data)

ex_b = part_b(example)
if ex_b == "":
    sys.exit(0)
check_example(ex_b, 6)
puzzle.answer_b = part_b(puzzle.input_data)
