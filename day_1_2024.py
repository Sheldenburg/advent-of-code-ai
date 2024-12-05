# aoc_template.py

import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser
import re
from collections import Counter

load_dotenv()

Part1 = os.getenv("Part1", "false").lower() == "true"


def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.strip().splitlines()
    left_list = []
    right_list = []
    for line in lines:
        l, r = map(int, line.split())
        left_list.append(l)
        right_list.append(r)
    return left_list, right_list


def part1(data):
    """Solve part 1."""
    left, right = data
    left.sort()
    right.sort()
    total_distance = 0
    for i in range(len(left)):
        total_distance += abs(left[i] - right[i])
    return total_distance


def part2(data):
    """Solve part 2."""
    left, right = data
    right_count = Counter(right)
    similarity_score = 0
    for num in left:
        similarity_score += num * right_count[num]
    return similarity_score


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
    path = "aoc_2024_day_1.txt"
    solve(pathlib.Path(path).read_text().strip())