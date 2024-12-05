# aoc_template.py

import pathlib
import sys
from aocd import get_data, submit
from dotenv import load_dotenv

# Load the session ID from the .env file
load_dotenv()

Part1 = False


def parse(puzzle_input):
    """Parse input."""
    reports = []
    for line in puzzle_input.strip().split("\n"):
        reports.append(list(map(int, line.split())))
    return reports


def is_safe(report):
    """Check if a report is safe."""
    increasing = all(
        report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3
        for i in range(len(report) - 1)
    )
    decreasing = all(
        report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3
        for i in range(len(report) - 1)
    )
    return increasing or decreasing


def is_safe_part2(report):
    """Check if a report is safe."""
    increasing = all(
        report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3
        for i in range(len(report) - 1)
    )
    decreasing = all(
        report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3
        for i in range(len(report) - 1)
    )
    return increasing or decreasing


def part1(data):
    """Solve part 1."""
    safe_count = sum(1 for report in data if is_safe(report))
    return safe_count


def part2(data):
    """Solve part 2."""

    def can_be_safe_by_removing_one(report):
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1 :]
            if is_safe_part2(modified_report):
                return True
        return False

    safe_count = 0
    for report in data:
        if is_safe(report) or can_be_safe_by_removing_one(report):
            safe_count += 1
    return safe_count


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    if Part1:
        solution1 = part1(data)
        print(solution1)
        submit(solution1, part="a", day=2, year=2024)
    else:
        solution2 = part2(data)
        print(solution2)
        submit(solution2, part="b", day=2, year=2024)


if __name__ == "__main__":
    path = "aoc_2024_day_2.txt"
    solve(pathlib.Path(path).read_text().strip())
