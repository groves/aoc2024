from math import floor
from collections import defaultdict
import sys
from aocd.models import Puzzle
from rich import inspect, print

puzzle = Puzzle(day=5, year=2024)


def part_a(input):
    orders, updates = input.split("\n\n")
    ordering = defaultdict(list)
    for line in orders.split("\n"):
        before, after = line.split("|")
        ordering[int(before)].append(int(after))
    sum = 0
    for update in updates.split("\n"):
        update = [int(u) for u in update.split(",")]
        out = False
        for i, u in enumerate(update):
            for after in ordering.get(u, []):
                if after in update[:i]:
                    out = True
                    break
            if out:
                break
        if not out:
            sum += update[floor(len(update) / 2)]
    return sum


def part_b(input):
    orders, updates = input.split("\n\n")
    rules = defaultdict(list)
    for line in orders.split("\n"):
        before, after = [int(x) for x in line.split("|")]
        rules[int(before)].append(int(after))
    sum = 0
    for update in updates.split("\n"):
        update = [int(u) for u in update.split(",")]
        ordered = []
        for u in update:
            insert_pos = len(ordered)
            for before in rules.get(u, []):
                if before in ordered:
                    before_pos = ordered.index(before)
                    if before_pos < insert_pos:
                        insert_pos = before_pos
            ordered.insert(insert_pos, u)

        if update != ordered:
            sum += ordered[len(ordered) // 2]
    return sum


def check_example(solver, input, expected):
    actual = solver(input)
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}' with input\n{input}")
        sys.exit(1)


for ex in puzzle.examples:
    print(ex.input_data)
example = puzzle.examples[0].input_data
check_example(part_a, example, 143)

poss_a = part_a(puzzle.input_data)
if poss_a == "":
    sys.exit(0)
puzzle.answer_a = part_a(puzzle.input_data)
check_example(part_b, example, 123)
puzzle.answer_b = part_b(puzzle.input_data)
