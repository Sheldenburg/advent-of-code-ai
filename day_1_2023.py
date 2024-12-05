# aoc_template.py

import pathlib
from dotenv import load_dotenv
import sys
from aocd import get_data, submit
from collections import Counter

load_dotenv()

Part1 = False

digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1."""
    total = 0
    for line in data:
        digits = [c for c in line if c.isdigit()]
        if digits:
            total += int(digits[0] + digits[-1])
    return total


def find_first_digit(line):
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]
        for digit, num in digit_map.items():
            if line[i : i + len(digit)] == digit:
                return num
    return None


def find_last_digit(line):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return line[i]
        for digit, num in digit_map.items():
            if line[i : i + len(digit)] == digit:
                return num
    return None


def part2(data):
    """Solve part 2."""
    total = 0
    for line in data:
        first_digit = find_first_digit(line)
        last_digit = find_last_digit(line)
        if first_digit and last_digit:
            total += int(first_digit + last_digit)
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    if Part1:
        solution = part1(data)
        submit(solution, part="a", day=1, year=2023)
    else:
        solution = part2(data)
        submit(solution, part="b", day=1, year=2023)


if __name__ == "__main__":
    path = "aoc_2023_day_1.txt"
    solve(pathlib.Path(path).read_text().strip())
