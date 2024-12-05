# aoc_template.py

import pathlib
from dotenv import load_dotenv
import sys
from aocd import get_data, submit
from collections import Counter

load_dotenv()

Part1 = False


def parse(puzzle_input):
    """Parse input."""
    left_list = []
    right_list = []
    for line in puzzle_input.strip().split("\n"):
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list


def part1(data):
    """Solve part 1."""
    left_list, right_list = data
    left_list.sort()
    right_list.sort()

    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance


def part2(data):
    """Solve part 2."""
    left_list, right_list = data
    right_count = Counter(right_list)

    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_count[num]

    return similarity_score


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    if Part1:
        solution = part1(data)
        submit(solution, part="a", day=1, year=2024)
    else:
        solution = part2(data)
        submit(solution, part="b", day=1, year=2024)


if __name__ == "__main__":
    path = "aoc_2024_day_1.txt"
    solve(pathlib.Path(path).read_text().strip())
