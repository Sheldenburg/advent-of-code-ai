# aoc_template.py

import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser
from collections import deque

load_dotenv()

Part1 = os.getenv("Part1", "true").lower() == "true"

DIRECTIONS = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}


def parse(puzzle_input):
    """Parse input."""
    return [list(line) for line in puzzle_input.splitlines()]


def find_start(data):
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "S":
                return (y, x)
    return None


def get_neighbors(y, x, data):
    pipetype = data[y][x]
    neighbors = []
    if pipetype == "S" or pipetype == ".":
        return neighbors

    for dy, dx in DIRECTIONS.get(pipetype, []):
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(data) and 0 <= nx < len(data[0]):
            npipetype = data[ny][nx]
            if npipetype != "." and (ny, nx) not in neighbors:
                neighbors.append((ny, nx))
    return neighbors


def bfs_farthest_point(start, data):
    queue = deque([(start, 0)])
    visited = set()
    max_distance = 0

    while queue:
        (y, x), dist = queue.popleft()
        if (y, x) in visited:
            continue
        visited.add((y, x))
        max_distance = max(max_distance, dist)

        for ny, nx in get_neighbors(y, x, data):
            if (ny, nx) not in visited:
                queue.append(((ny, nx), dist + 1))

    return max_distance


def part1(data):
    """Solve part 1."""
    start_position = find_start(data)
    if start_position is None:
        return 0
    return bfs_farthest_point(start_position, data)


def part2(data):
    """Solve part 2."""
    pass  # Part 2 implementation pending


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    config = configparser.ConfigParser()
    config.read("config.ini")
    day = config.getint("DEFAULT", "day")
    year = config.getint("DEFAULT", "year")

    if Part1:
        solution = part1(data)
        print(solution)
        # submit(solution, part="a", day=day, year=year)
    else:
        solution = part2(data)
        submit(solution, part="b", day=day, year=year)


if __name__ == "__main__":
    path = "aoc_2023_day_10.txt"
    solve(pathlib.Path(path).read_text().strip())
