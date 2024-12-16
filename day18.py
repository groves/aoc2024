from collections import defaultdict
import heapq
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=18, year=2024)


dirs = {(1, 0), (-1, 0), (0, 1), (0, -1)}


def solve(input, size, time):
    corrupted = {
        tuple([int(i) for i in s.split(",")])
        for step, s in enumerate(input.splitlines())
        if step < time
    }
    nodes = set()
    adjacency = defaultdict(set)
    for r in range(size):
        for c in range(size):
            if (c, r) in corrupted:
                continue
            node = (r, c)
            nodes.add(node)
            for rm, cm in dirs:
                rn, cn = r + rm, c + cm
                if (
                    cn >= 0
                    and cn < size
                    and rn >= 0
                    and rn < size
                    and (cn, rn) not in corrupted
                ):
                    adjacency[node].add(((rn, cn), 1))

    return djikstra(nodes, adjacency, (0, 0), (size - 1, size - 1))


def djikstra(nodes, adjacency, start, end):
    distances = {node: (0 if node == start else float("inf")) for node in nodes}

    pq = [(0, start)]
    while len(pq) > 0:
        dist, current = heapq.heappop(pq)

        if dist > distances[current]:
            continue
        for neighbor, distance in adjacency[current]:
            dn = distances[current] + distance
            if dn < distances[neighbor]:
                distances[neighbor] = dn
                heapq.heappush(pq, (dn, neighbor))

    return distances[end]


def part_b(input, size, time):
    while solve(input, size, time) != float("inf"):
        time += 1
    return input.splitlines()[time - 1]


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = puzzle.examples[0].input_data

check_example(
    solve(example, 7, 12),
    22,
)
puzzle.answer_a = solve(puzzle.input_data, 71, 1024)

check_example(part_b(example, 7, 12), "6,1")
puzzle.answer_b = part_b(puzzle.input_data, 71, 1024)
