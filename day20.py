from collections import defaultdict
import heapq
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=20, year=2024)


dirs = {(1, 0), (-1, 0), (0, 1), (0, -1)}


def solve(maze):
    nodes = set()
    adjacency = defaultdict(set)
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "#":
                continue
            node = (r, c)
            nodes.add(node)
            for rm, cm in dirs:
                rn, cn = r + rm, c + cm
                if maze[rn][cn] != "#":
                    adjacency[node].add(((rn, cn), 1))
            if maze[r][c] == "S":
                start = r, c
            if maze[r][c] == "E":
                end = r, c

    return djikstra(nodes, adjacency, start, end), end


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

    return distances


def count_cheats(input, min_saved, cheat_allowed):
    maze = [list(line) for line in input.splitlines()]
    distances, _ = solve(maze)
    cheats = defaultdict(int)
    for (r, c), d in distances.items():
        for (ro, co), do in distances.items():
            rd, cd = abs(r - ro), abs(c - co)
            total = rd + cd
            if total == 0 or total > cheat_allowed or (do - total) <= d + 1:
                continue
            cheats[do - d - total] += 1
    return sum(v for k, v in cheats.items() if k >= min_saved)


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


example = puzzle.examples[0].input_data

check_example(count_cheats(example, 40, 2), 2)
puzzle.answer_a = count_cheats(puzzle.input_data, 100, 2)

check_example(count_cheats(example, 74, 20), 7)
puzzle.answer_b = count_cheats(puzzle.input_data, 100, 20)
