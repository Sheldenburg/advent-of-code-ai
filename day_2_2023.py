# aoc_template.py

import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser
import re

load_dotenv()

Part1 = os.getenv("Part1", "false").lower() == "true" # Set to false for part 2


def parse(puzzle_input):
    """Parse input."""
    games = []
    for line in puzzle_input.splitlines():
        match = re.match(r"Game (\d+): (.*)", line)
        game_id = int(match.group(1))
        sets = match.group(2).split("; ")
        game_sets = []
        for s in sets:
            cubes = {}
            for c in s.split(", "):
                count, color = c.split()
                cubes[color] = int(count)
            game_sets.append(cubes)
        games.append((game_id, game_sets))
    return games


def part1(data):
    """Solve part 1."""
    max_red = 12
    max_green = 13
    max_blue = 14
    total = 0
    for game_id, sets in data:
        possible = True
        for s in sets:
            if s.get("red", 0) > max_red or s.get("green", 0) > max_green or s.get("blue", 0) > max_blue:
                possible = False
                break
        if possible:
            total += game_id
    return total


def part2(data):
    """Solve part 2."""
    total_power = 0
    for game_id, sets in data:
        max_red = 0
        max_green = 0
        max_blue = 0
        for s in sets:
            max_red = max(max_red, s.get("red", 0))
            max_green = max(max_green, s.get("green", 0))
            max_blue = max(max_blue, s.get("blue", 0))
        total_power += max_red * max_green * max_blue
    return total_power


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
        submit(solution, part="b", day=day, year=year)


if __name__ == "__main__":
    path = "aoc_2023_day_2.txt"
    solve(pathlib.Path(path).read_text().strip())