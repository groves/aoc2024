import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=9, year=2024)


def parse(input):
    nums = [int(c) for c in input]
    blocks = [None] * sum(nums)
    initial_used = []
    pos = 0
    id = 0
    free = False
    total_used = 0
    for num in nums:
        if not free:
            for i in range(pos, pos + num):
                blocks[i] = id
            initial_used.append((pos, num, id))
            total_used += num
            id += 1
        pos += num
        free = not free
    return blocks, initial_used, total_used


def part_a(input):
    blocks, _, total_used = parse(input)
    last_empty = 0
    last_used = len(blocks) - 1
    while last_used > total_used:
        while blocks[last_used] is None:
            last_used -= 1
        while blocks[last_empty] is not None:
            last_empty += 1
        blocks[last_empty], blocks[last_used] = blocks[last_used], None
    return sum(i * num for i, num in enumerate(blocks) if num is not None)


def part_b(input):
    blocks, initial_used, _ = parse(input)
    for pos, size, id in reversed(initial_used):
        free_size, start = 0, None
        for i, c in enumerate(blocks):
            if pos < i:
                break
            if c is None:
                if start is None:
                    start = i
                free_size += 1
                if free_size == size:
                    for off in range(size):
                        blocks[start + off] = id
                        blocks[pos + off] = None
                    break
            else:
                start = None
                free_size = 0

    return sum(i * num for i, num in enumerate(blocks) if num is not None)


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = puzzle.examples[0].input_data

check_example(part_a(example), 1928)
puzzle.answer_a = part_a(puzzle.input_data)

check_example(part_b(example), 2858)
puzzle.answer_b = part_b(puzzle.input_data)
