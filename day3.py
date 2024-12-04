from aocd.models import Puzzle
from rich import print
import re

puzzle = Puzzle(day=3, year=2024)


def part_b(input):
    sum = 0
    enabled = True
    for line in input.splitlines():
        for m in re.finditer(
            "(?P<e>do(?P<d>n't)?\\(\\))|(mul\\((?P<a>\\d{1,3}),(?P<b>\\d{1,3})\\))",
            line,
        ):
            groups = m.groupdict()
            if groups["a"] is not None:
                if enabled:
                    sum += int(groups["a"]) * int(groups["b"])
            else:
                enabled = groups["d"] is None
    return sum


def check_example(solver, input, expected):
    actual = solver(input)
    if isinstance(actual, int):
        actual = str(actual)
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}' with input\n{input}")
        import sys

        sys.exit(1)


for example in puzzle.examples:
    if example.answer_b is not None:
        check_example(
            part_b,
            """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))""",
            "48",
        )

poss_b = part_b(puzzle.input_data)
if poss_b != "":
    puzzle.answer_b = poss_b
