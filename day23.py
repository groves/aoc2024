from collections import defaultdict
import re
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=23, year=2024)


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


def part_a(input):
    triples = set()
    conns = defaultdict(set)
    for line in input.splitlines():
        a, b = line.split("-")
        conns[a].add(b)
        conns[b].add(a)
    for a, bs in conns.items():
        for b in bs:
            for c in conns[b]:
                if c in bs:
                    triples.add(tuple(sorted([a, b, c])))
    return len([t for t in triples if any(i.startswith("t") for i in t)])


def bron_kerbosch(clique, candidates, processed, graph):
    if not candidates and not processed:
        yield clique
    while candidates:
        v = candidates.pop()
        yield from bron_kerbosch(
            clique | {v}, candidates & graph[v], processed & graph[v], graph
        )
        processed.add(v)


def max_clique(graph):
    nodes = set(graph.keys())
    max_clique = []
    for clique in bron_kerbosch(set(), nodes, set(), graph):
        if len(clique) > len(max_clique):
            max_clique = clique
    return max_clique


def part_b(input):
    conns = defaultdict(set)
    for line in input.splitlines():
        a, b = line.split("-")
        conns[a].add(b)
        conns[b].add(a)

    bigboy = max_clique(conns)
    return ",".join(sorted(bigboy))


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = puzzle.examples[0].input_data

check_example(part_a(example), 7)
puzzle.answer_a = part_a(puzzle.input_data)

check_example(part_b(example), "co,de,ka,ta")
puzzle.answer_b = part_b(puzzle.input_data)
