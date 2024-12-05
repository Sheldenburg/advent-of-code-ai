# aoc_template.py

import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser
import re

load_dotenv()

Part1 = False  # Set to False for Part 2


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data):
    """Solve part 1."""
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)
    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])
    return total


def part2(data):
    """Solve part 2."""
    # Regex to match mul and do/don't instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"(do\(\)|don't\(\))"

    # Find all mul and control instructions in sequence
    instructions = re.findall(f"{control_pattern}|{mul_pattern}", data)

    # Track whether mul instructions are enabled
    enabled = True
    total = 0

    for instruction in instructions:
        if instruction[0]:  # If it's a control instruction
            if instruction[0] == "do()":
                enabled = True
            elif instruction[0] == "don't()":
                enabled = False
        elif instruction[1] and instruction[2]:  # If it's a mul instruction
            if enabled:
                total += int(instruction[1]) * int(instruction[2])

    return total


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
        print(solution)
        submit(solution, part="b", day=day, year=year)


if __name__ == "__main__":
    path = "aoc_2024_day_3.txt"
    puzzle_input = pathlib.Path(path).read_text().strip()
    solve(puzzle_input)
