# aoc_template.py

import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser

load_dotenv()

Part1 = os.getenv("Part1", "true").lower() == "true"


def parse(puzzle_input):
    """Parse input."""


def part1(data):
    """Solve part 1."""


def part2(data):
    """Solve part 2."""


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
    path = "aoc_2023_day_x.txt"
    solve(pathlib.Path(path).read_text().strip())
