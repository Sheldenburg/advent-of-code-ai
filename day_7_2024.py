# aoc_template.py

import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser
from itertools import product

load_dotenv()

Part1 = os.getenv("Part1", "true").lower() == "true"

def parse(puzzle_input):
    """Parse input."""
    equations = []
    lines = puzzle_input.split('\n')
    for line in lines:
        if line:
            test_value, numbers = line.split(':')
            numbers = list(map(int, numbers.split()))
            equations.append((int(test_value), numbers))
    return equations

def evaluate(numbers, operators):
    """Evaluate the expression with given operators."""
    result = str(numbers[0])
    for i, op in enumerate(operators):
        if op == '+':
            result = str(int(result) + numbers[i + 1])
        elif op == '*':
            result = str(int(result) * numbers[i + 1])
        elif op == '||':
            result += str(numbers[i+1])
    return int(result)

def possible_equation(test_value, numbers):
    """Check if a combination of operators can result in the test value."""
    n = len(numbers) - 1
    for ops in product(['+', '*', '||'], repeat=n):
        try:
            if evaluate(numbers, ops) == test_value:
                return True
        except ValueError: #Handles cases where concatenation results in a number too large for int
            pass
    return False

def part1(data):
    """Solve part 1."""
    total_calibration_result = 0
    for test_value, numbers in data:
        if possible_equation(test_value, numbers):
            total_calibration_result += test_value
    return total_calibration_result

def part2(data):
    return part1(data) #Part 2 uses the same function with extended operators


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
    path = "aoc_2024_day_7.txt"
    solve(pathlib.Path(path).read_text().strip())