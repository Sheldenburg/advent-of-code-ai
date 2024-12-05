# aoc_template.py

import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser

load_dotenv()

Part1 = os.getenv("Part1", "false").lower() == "true"


def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.splitlines()
    cards = []
    for line in lines:
        card_data = line.split(": ")[1]
        winning_numbers, my_numbers = card_data.split(" | ")
        winning_numbers = set(map(int, winning_numbers.split()))
        my_numbers = set(map(int, my_numbers.split()))
        cards.append((winning_numbers, my_numbers))
    return cards


def part1(data):
    """Solve part 1."""
    total_points = 0
    for winning_numbers, my_numbers in data:
        matches = len(winning_numbers.intersection(my_numbers))
        if matches > 0:
            points = 2**(matches - 1)
            total_points += points
    return total_points


def part2(data):
    """Solve part 2."""
    card_counts = [1] * len(data)
    for i, (winning_numbers, my_numbers) in enumerate(data):
        matches = len(winning_numbers.intersection(my_numbers))
        for j in range(i + 1, min(i + 1 + matches, len(data))):
            card_counts[j] += card_counts[i]
    return sum(card_counts)


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
    path = "aoc_2023_day_4.txt"
    solve(pathlib.Path(path).read_text().strip())