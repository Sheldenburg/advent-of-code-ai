# aoc_template.py

import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser
import re

load_dotenv()

Part1 = os.getenv("Part1", "true").lower() == "true"


def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.splitlines()
    data = []
    for line in lines:
        match = re.match(r"([?.#]+)\s+([\d,]+)", line)
        springs = match.group(1)
        groups = [int(x) for x in match.group(2).split(',')]
        data.append((springs, groups))
    return data


def count_arrangements(springs, groups):
    count = 0
    
    def backtrack(index, current_arrangement, remaining_groups):
        nonlocal count
        if index == len(springs):
            if not remaining_groups:
                count += 1
            return

        if springs[index] == '?':
            # Try both '#' and '.'
            backtrack(index + 1, current_arrangement + '#', remaining_groups)
            backtrack(index + 1, current_arrangement + '.', remaining_groups)
        else:
            backtrack(index + 1, current_arrangement + springs[index], remaining_groups)

    def check_arrangement(arrangement):
        group_lengths = []
        current_length = 0
        for i in range(len(arrangement)):
            if arrangement[i] == '#':
                current_length +=1
            else:
                if current_length > 0:
                    group_lengths.append(current_length)
                    current_length = 0
        if current_length > 0:
            group_lengths.append(current_length)
        return group_lengths == groups

    backtrack(0, "", groups)
    return count


def part1(data):
    """Solve part 1."""
    total_arrangements = 0
    for springs, groups in data:
        total_arrangements += count_arrangements(springs, groups)
    return total_arrangements


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
    path = "aoc_2023_day_12.txt"
    puzzle_input = pathlib.Path(path).read_text().strip()
    solve(puzzle_input)