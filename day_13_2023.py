# aoc_template.py

import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser

load_dotenv()

Part1 = os.getenv("Part1", "true").lower() == "true"


def parse(puzzle_input):
    """Parse input into a list of patterns."""
    patterns = puzzle_input.strip().split("\n\n")
    return [pattern.splitlines() for pattern in patterns]


def part1(data):
    """Solve part 1."""
    total_summary = 0
    
    for pattern in data:
        n_rows = len(pattern)
        n_cols = len(pattern[0])
        
        # Check for vertical mirror
        for mid in range(1, n_cols):
            is_vertical_mirror = True
            for row in pattern:
                left_part = row[:mid]
                right_part = row[mid:]
                
                if left_part != right_part[::-1]:
                    is_vertical_mirror = False
                    break
            
            if is_vertical_mirror:
                total_summary += mid
                break
        
        # Check for horizontal mirror
        for mid in range(1, n_rows):
            upper_part = pattern[:mid]
            lower_part = pattern[mid:]
            
            if upper_part == lower_part[::-1]:
                total_summary += 100 * mid
                break
    
    return total_summary


def part2(data):
    """Solve part 2."""
    pass  # Not needed for Part 1


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    config = configparser.ConfigParser()
    config.read("config.ini")
    day = config.getint("DEFAULT", "day")
    year = config.getint("DEFAULT", "year")

    if Part1:
        solution = part1(data)
        print(f"Part 1 solution: {solution}")
        submit(solution, part="a", day=day, year=year)
    else:
        solution = part2(data)
        print(f"Part 2 solution: {solution}")
        submit(solution, part="b", day=day, year=year)


if __name__ == "__main__":
    path = "aoc_2023_day_13.txt"
    solve(pathlib.Path(path).read_text().strip())