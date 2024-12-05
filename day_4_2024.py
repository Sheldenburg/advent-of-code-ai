# aoc_template.py

import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser

load_dotenv()

Part1 = os.getenv("Part1", "false").lower() == "true"


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data):
    """Solve part 1."""
    grid = []
    for line in data.splitlines():
        grid.append(list(line))

    count = 0
    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"

    for r in range(rows):
        for c in range(cols):
            # Check horizontal
            if c + 4 <= cols:
                if "".join(grid[r][c : c + 4]) == target:
                    count += 1
                if "".join(grid[r][c : c + 4][::-1]) == target:
                    count += 1

            # Check vertical
            if r + 4 <= rows:
                word = ""
                for i in range(4):
                    word += grid[r + i][c]
                if word == target:
                    count += 1
                word = ""
                for i in range(4):
                    word += grid[r + i][c]
                if word[::-1] == target:
                    count += 1

            # Check diagonals (top-left to bottom-right)
            if r + 4 <= rows and c + 4 <= cols:
                word = ""
                for i in range(4):
                    word += grid[r + i][c + i]
                if word == target:
                    count += 1
                word = ""
                for i in range(4):
                    word += grid[r + i][c + i]
                if word[::-1] == target:
                    count += 1

            # Check diagonals (top-right to bottom-left)
            if r + 4 <= rows and c - 3 >= 0:
                word = ""
                for i in range(4):
                    word += grid[r + i][c - i]
                if word == target:
                    count += 1
                word = ""
                for i in range(4):
                    word += grid[r + i][c - i]
                if word[::-1] == target:
                    count += 1

    return count


def part2(data):
    """Solve part 2."""
    grid = []
    for line in data.splitlines():
        grid.append(list(line))
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Define the patterns for "X-MAS"
    mas_forward = "MAS"
    mas_backward = "SAM"

    # Iterate through every cell in the grid except edges
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Extract the diagonals
            diagonal1 = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
            diagonal2 = grid[i + 1][j - 1] + grid[i][j] + grid[i - 1][j + 1]

            # Check if both diagonals match the pattern
            if diagonal1 in {mas_forward, mas_backward} and diagonal2 in {
                mas_forward,
                mas_backward,
            }:
                count += 1

    return count


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    config = configparser.ConfigParser()
    config.read("config.ini")
    day = config.getint("DEFAULT", "day")
    year = config.getint("DEFAULT", "year")

    if Part1:
        solution = part1(data)
        submit(solution, part="a", day=day, year=year)
    else:
        solution = part2(data)
        print(solution)
        submit(solution, part="b", day=day, year=year)


if __name__ == "__main__":
    path = "aoc_2024_day_4.txt"
    solve(pathlib.Path(path).read_text().strip())
