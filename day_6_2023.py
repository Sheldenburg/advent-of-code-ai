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
    time = int("".join(lines[0].split(":")[1].strip().split()))
    distance = int("".join(lines[1].split(":")[1].strip().split()))
    return time, distance


def part1(data):
    """Solve part 1."""
    times, distances = data
    ways_to_win = []
    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        count = 0
        for hold_time in range(1, time):
            travel_time = time - hold_time
            distance_traveled = hold_time * travel_time
            if distance_traveled > distance:
                count += 1
        ways_to_win.append(count)
    result = 1
    for num in ways_to_win:
        result *= num
    return result


def part2(data):
    """Solve part 2."""
    time, distance = data
    count = 0
    for hold_time in range(1, time):
        travel_time = time - hold_time
        distance_traveled = hold_time * travel_time
        if distance_traveled > distance:
            count += 1
    return count


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
    path = "aoc_2023_day_6.txt"
    solve(pathlib.Path(path).read_text().strip())