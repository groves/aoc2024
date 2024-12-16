import heapq
from collections import defaultdict, deque
import inspect
import re
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=16, year=2024)


def dbg(vars):
    frame = inspect.currentframe().f_back
    print(*[f"{var}={frame.f_locals[var]}" for var in vars.split(" ")])


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


dirs = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}
turns = {"v": ["<", ">"], "^": ["<", ">"], ">": ["^", "v"], "<": ["^", "v"]}


def solve(input):
    maze = [list(line) for line in input.splitlines()]
    rs, cs = len(maze), len(maze[0])
    nodes = set()
    adjacency = defaultdict(set)
    for r in range(rs):
        for c in range(cs):
            if maze[r][c] == "#":
                continue
            for dir, (rm, cm) in dirs.items():
                node = (r, c, dir)
                nodes.add(node)
                for turn in turns[dir]:
                    adjacency[node].add(((r, c, turn), 1000))
                rn, cn = r + rm, c + cm
                if maze[rn][cn] != "#":
                    adjacency[node].add(((rn, cn, dir), 1))
                if maze[r][c] == "S" and dir == ">":
                    start = node
            if maze[r][c] == "E":
                end = r, c
    return djikstra(nodes, adjacency, start, end)


def djikstra(nodes, adjacency, start, end):
    distances = {node: (0 if node == start else float("inf")) for node in nodes}

    pq = [(0, start)]
    while len(pq) > 0:
        _, current = heapq.heappop(pq)

        for neighbor, distance in adjacency[current]:
            dn = distances[current] + distance
            if dn < distances[neighbor]:
                distances[neighbor] = dn
            if dn <= distances[neighbor]:
                heapq.heappush(pq, (dn, neighbor))

    visited = set()
    min_end = None

    for (r, c, _), cost in distances.items():
        if (r, c) == end:
            if min_end is None or cost < min_end:
                min_end = cost
    for (r, c, d), cost in distances.items():
        if (r, c) == end and cost == min_end:
            walk((r, c, d), visited, distances, start)

    return visited, min_end


def walk(pos, visited, distances, start):
    r, c, d = pos
    visited.add((r, c))
    if pos == start:
        return
    min_prev = None
    poss = [(r, c, dn) for dn in turns[d]]
    rm, cm = dirs[d]
    poss.append((r - rm, c - cm, d))
    best = None
    for p in poss:
        prev = distances.get(p)
        if prev is not None:
            prev += 1 if p[2] == d else 1000
            if min_prev is None or prev < min_prev:
                best = [p]
                min_prev = prev
            elif prev == min_prev:
                best.append(p)
    for p in best:
        walk(p, visited, distances, start)


def part_a(input):
    return solve(input)[1]


def part_b(input):
    return len(solve(input)[0])


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


ex1 = puzzle.examples[0].input_data
ex2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

check_example(part_a(ex2), 11048)
check_example(part_a(ex1), 7036)
puzzle.answer_a = part_a(puzzle.input_data)

check_example(part_b(ex1), 45)
check_example(part_b(ex2), 64)
puzzle.answer_b = part_b(puzzle.input_data)
