import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser
import math

load_dotenv()

Part1 = os.getenv("Part1", "true").lower() == "true"


def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.splitlines()
    return lines


def part1(data):
    """Solve part 1."""
    antennas = {}
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char.isalnum():
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((r, c))

    antinode_locations = set()
    for freq, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                r1, c1 = coords[i]
                r2, c2 = coords[j]

                dr, dc = r2 - r1, c2 - c1
                dist = (dr**2 + dc**2) ** 0.5

                if dist > 0:  # avoid antennas at the same position
                    if (
                        abs(dist - 2 * (dist / 2)) < 1e-6
                    ):  # check if one is twice the distance from the other
                        antinode1_r, antinode1_c = r1 - dr, c1 - dc
                        antinode2_r, antinode2_c = r2 + dr, c2 + dc

                        if 0 <= antinode1_r < len(data) and 0 <= antinode1_c < len(
                            data[0]
                        ):
                            antinode_locations.add((antinode1_r, antinode1_c))

                        if 0 <= antinode2_r < len(data) and 0 <= antinode2_c < len(
                            data[0]
                        ):
                            antinode_locations.add((antinode2_r, antinode2_c))

    return len(antinode_locations)


def part2(data):
    """
    Solve part 2: Calculate the number of unique antinode locations.

    An antinode occurs at any grid position that lies exactly on a straight line
    connecting at least two antennas of the same frequency. Each antenna also
    counts as an antinode if it is aligned with at least one other antenna
    of the same frequency.
    """
    # Parse the input to map antenna frequencies to their coordinates
    antennas = {}
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char.isalnum():  # Check if it's a valid frequency
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((r, c))

    # Set to store all unique antinode locations
    antinode_locations = set()

    # Process each frequency group of antennas
    for freq, coords in antennas.items():
        # Add all antenna positions as antinodes initially
        for coord in coords:
            antinode_locations.add(coord)

        # Compare every pair of antennas for this frequency
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                r1, c1 = coords[i]
                r2, c2 = coords[j]

                # Compute the differences in rows and columns
                dr, dc = r2 - r1, c2 - c1

                # Calculate the GCD of dr and dc to determine step size
                gcd = (
                    abs(dr)
                    if dc == 0
                    else abs(dc)
                    if dr == 0
                    else abs(math.gcd(dr, dc))
                )
                step_r, step_c = dr // gcd, dc // gcd

                # Generate all points along the line between antennas
                r, c = r1, c1
                while 0 <= r < len(data) and 0 <= c < len(data[0]):
                    antinode_locations.add((r, c))
                    r += step_r
                    c += step_c

                # Check backward points along the line
                r, c = r1 - step_r, c1 - step_c
                while 0 <= r < len(data) and 0 <= c < len(data[0]):
                    antinode_locations.add((r, c))
                    r -= step_r
                    c -= step_c

    # Return the count of unique antinode locations
    return len(antinode_locations)


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
        print(solution)
    else:
        solution = part2(data)
        submit(solution, part="b", day=day, year=year)
        print(solution)


if __name__ == "__main__":
    path = "aoc_2024_day_8.txt"  # replace with your input file name
    solve(pathlib.Path(path).read_text().strip())
