import itertools
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=4, year=2024)


def check(grid, r, c, rstep, cstep, letter="X"):
    if grid[r][c] != letter:
        return 0
    if letter == "S":
        return 1
    next = {"X": "M", "M": "A", "A": "S"}[letter]
    nr = r + rstep
    nc = c + cstep
    if nr >= len(grid) or nr < 0 or nc >= len(grid[0]) or nc < 0:
        return 0
    return check(grid, nr, nc, rstep, cstep, next)


def part_a(input):
    xmases = 0
    grid = []
    for line in input.splitlines():
        grid.append(line)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            for rstep, cstep in itertools.product([-1, 0, 1], repeat=2):
                if rstep == 0 and cstep == 0:
                    continue
                xmases += check(grid, r, c, rstep, cstep)

    return xmases


def part_b(input):
    xmases = 0
    grid = []
    for line in input.splitlines():
        grid.append(line)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (
                grid[r][c] != "A"
                or r == 0
                or r == len(grid) - 1
                or c == 0
                or c == len(grid[0]) - 1
            ):
                continue
            if grid[r - 1][c - 1] == "M":
                if grid[r + 1][c + 1] != "S":
                    continue
            elif grid[r - 1][c - 1] == "S":
                if grid[r + 1][c + 1] != "M":
                    continue
            else:
                continue
            if grid[r + 1][c - 1] == "M":
                if grid[r - 1][c + 1] != "S":
                    continue
            elif grid[r + 1][c - 1] == "S":
                if grid[r - 1][c + 1] != "M":
                    continue
            else:
                continue
            xmases += 1

    return xmases


def check_example(solver, input, expected):
    actual = solver(input)
    if isinstance(actual, int):
        actual = str(actual)
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}' with input\n{input}")
        import sys

        sys.exit(1)


example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

check_example(part_a, example, "18")
check_example(part_b, example, "9")

poss_a = part_a(puzzle.input_data)
if poss_a != "":
    puzzle.answer_a = part_a(puzzle.input_data)
poss_b = part_b(puzzle.input_data)
if poss_b != "":
    puzzle.answer_b = part_b(puzzle.input_data)
