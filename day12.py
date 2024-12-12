from collections import defaultdict
from itertools import chain
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=12, year=2024)


def add(spanholder, less, idx, low):
    spans = spanholder[(less, idx)]
    low_conjoin = None
    high_conjoin = None
    for span in spans:
        if span[0] == low + 1:
            low_conjoin = span
        if span[1] == low:
            high_conjoin = span
    if low_conjoin is None:
        if high_conjoin is None:
            spans.append([low, low + 1])
        else:
            high_conjoin[1] += 1
    elif high_conjoin is None:
        low_conjoin[0] = low
    else:
        spans.remove(low_conjoin)
        high_conjoin[1] = low_conjoin[1]


def visit(rows, rs, cs, visited, horizontals, verticals, r, c):
    visited.add((r, c))
    perimeter = 0
    area = 1

    for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if rn == -1 or rn == rs or cn == -1 or cn == cs or rows[rn][cn] != rows[r][c]:
            perimeter += 1
            if rn != r:
                add(horizontals, rn < r, r if rn < r else rn, c)
            if cn != c:
                add(verticals, cn < c, c if cn < c else cn, r)
        elif (rn, cn) not in visited:
            an, pn = visit(rows, rs, cs, visited, horizontals, verticals, rn, cn)
            area += an
            perimeter += pn
    return area, perimeter


def part_a(input):
    rows = input.splitlines()
    rs, cs = len(rows), len(rows[0])
    visited = set()
    result = 0
    for r in range(rs):
        for c in range(cs):
            if (r, c) not in visited:
                area, perimeter = visit(
                    rows, rs, cs, visited, defaultdict(list), defaultdict(list), r, c
                )
                result += area * perimeter
    return result


def part_b(input):
    rows = input.splitlines()
    rs, cs = len(rows), len(rows[0])
    visited = set()
    result = 0
    for r in range(rs):
        for c in range(cs):
            if (r, c) not in visited:
                horizontals, verticals = defaultdict(list), defaultdict(list)
                area, perimeter = visit(
                    rows, rs, cs, visited, horizontals, verticals, r, c
                )
                sides = 0
                for segments in chain(horizontals.values(), verticals.values()):
                    sides += len(segments)
                result += area * sides
    return result


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example1 = (
    """AAAA
BBCD
BBCC
EEEC""",
    140,
    80,
)
example2 = (
    """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""",
    1930,
    1206,
)

examples = [example1, example2]

for input, answer1, _ in examples:
    check_example(part_a(input), answer1)
puzzle.answer_a = part_a(puzzle.input_data)

for input, _, answer2 in examples:
    check_example(part_b(input), answer2)
check_example(
    part_b(
        """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA""",
    ),
    368,
)
puzzle.answer_b = part_b(puzzle.input_data)
