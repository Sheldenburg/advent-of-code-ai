# aoc_template.py

import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser
from copy import deepcopy

load_dotenv()

Part1 = os.getenv("Part1", "true").lower() == "true"


def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split("\n")
    grid = [list(line) for line in lines]
    return grid


def move_guard(grid, direction, x, y):
    if direction == "^":
        return (x - 1, y)
    elif direction == ">":
        return (x, y + 1)
    elif direction == "v":
        return (x + 1, y)
    elif direction == "<":
        return (x, y - 1)


def turn_right(direction):
    if direction == "^":
        return ">"
    elif direction == ">":
        return "v"
    elif direction == "v":
        return "<"
    elif direction == "<":
        return "^"


def part1(grid):
    """Solve part 1."""
    directions = ["^", ">", "v", "<"]
    height = len(grid)
    width = len(grid[0])

    # Find guard's starting position and direction
    x = y = None
    direction = None
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val in directions:
                x, y = i, j
                direction = val
                break
        if direction:
            break

    visited = set()
    visited.add((x, y))

    while 0 <= x < height and 0 <= y < width:
        new_x, new_y = move_guard(grid, direction, x, y)
        # if the new position is out of bounds, stop
        if not (0 <= new_x < height and 0 <= new_y < width):
            break

        # If there's an obstacle, turn right
        if grid[new_x][new_y] == "#":
            direction = turn_right(direction)
        else:
            # If path is clear, move forward
            x, y = new_x, new_y
            visited.add((x, y))

    return len(visited)


def part2(grid):
    """Solve part 2."""
    directions = ["^", ">", "v", "<"]
    height = len(grid)
    width = len(grid[0])

    # Find guard's starting position and direction
    x, y = None, None
    direction = None
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val in directions:
                x, y = i, j
                direction = val
                break
        if direction:
            break

    loop_positions = set()
    for i in range(height):
        for j in range(width):
            if grid[i][j] == ".":
                # Place a new obstruction at (i, j)
                new_grid = deepcopy(grid)
                new_grid[i][j] = "#"

                visited_states = set()
                cur_x, cur_y = x, y
                cur_dir = direction
                steps = 0
                max_steps = 10000  # Prevent infinite loops

                while 0 <= cur_x < height and 0 <= cur_y < width and steps < max_steps:
                    state = (cur_x, cur_y, cur_dir)
                    if state in visited_states:
                        # Loop detected
                        loop_positions.add((i, j))
                        break
                    visited_states.add(state)

                    # Move the guard
                    next_x, next_y = move_guard(new_grid, cur_dir, cur_x, cur_y)
                    if not (0 <= next_x < height and 0 <= next_y < width):
                        break
                    if new_grid[next_x][next_y] == "#":
                        cur_dir = turn_right(cur_dir)
                    else:
                        cur_x, cur_y = next_x, next_y

                    steps += 1

    return len(loop_positions)


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
        submit(solution, part="a", day=day, year=year)
    else:
        solution = part2(data)
        print(solution)
        submit(solution, part="b", day=day, year=year)


if __name__ == "__main__":
    path = "aoc_2024_day_6.txt"  # Change to "input.txt" for actual input
    solve(pathlib.Path(path).read_text().strip())
