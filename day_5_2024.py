import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser

load_dotenv()

Part1 = os.getenv("Part1", "false").lower() == "true"


def parse(puzzle_input):
    """Parse input."""
    sections = puzzle_input.split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(","))) for line in sections[1].splitlines()]
    return rules, updates


def part1(data):
    """Solve part 1."""
    rules, updates = data
    correctly_ordered_updates = []
    for update in updates:
        valid = True
        for x, y in rules:
            if x in update and y in update:
                if update.index(x) >= update.index(y):
                    valid = False
                    break
        if valid:
            correctly_ordered_updates.append(update)

    # Compute the middle page numbers sum
    middle_page_sum = sum(
        update[len(update) // 2] for update in correctly_ordered_updates
    )
    return middle_page_sum


def part2(data):
    """Solve part 2."""
    rules, updates = data
    incorrectly_ordered_updates = []
    for update in updates:
        valid = True
        for x, y in rules:
            if x in update and y in update:
                if update.index(x) >= update.index(y):
                    valid = False
                    break
        if not valid:
            incorrectly_ordered_updates.append(update)

    middle_page_sum = 0
    for update in incorrectly_ordered_updates:
        # Sort the update based on rules
        sorted_update = sorted(
            update,
            key=lambda x: (sum(1 for a, b in rules if a == x and b in update), x),
        )
        middle_page_sum += sorted_update[len(sorted_update) // 2]

    return middle_page_sum


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
        # submit(solution, part="b", day=day, year=year)
        print(solution)


if __name__ == "__main__":
    path = "aoc_2024_day_5.txt"  # Replace with your input file.  Make sure this file is in the same directory.
    solve(pathlib.Path(path).read_text().strip())
