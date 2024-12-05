# aoc_template.py

import pathlib
from dotenv import load_dotenv
import os
from aocd import submit
import configparser
import re

load_dotenv()

Part1 = os.getenv("Part1", "true").lower() == "true"


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        lines = f.read().splitlines()

    seeds = list(map(int, lines[0].split(": ")[1].split()))

    maps = {}
    current_map = None
    for line in lines[1:]:
        if line.strip() == "":
            continue
        if "map" in line:
            current_map = line.split(" ")[0]
            maps[current_map] = []
        else:
            maps[current_map].append(list(map(int, line.split())))

    return seeds, maps


def find_destination(source, mappings):
    for dest_start, source_start, length in mappings:
        if source_start <= source < source_start + length:
            return dest_start + (source - source_start)
    return source


def part1(data):
    """Solve part 1."""
    seeds, maps = data
    locations = []

    for seed in seeds:
        soil = find_destination(seed, maps["seed-to-soil"])
        fertilizer = find_destination(soil, maps["soil-to-fertilizer"])
        water = find_destination(fertilizer, maps["fertilizer-to-water"])
        light = find_destination(water, maps["water-to-light"])
        temperature = find_destination(light, maps["light-to-temperature"])
        humidity = find_destination(temperature, maps["temperature-to-humidity"])
        location = find_destination(humidity, maps["humidity-to-location"])
        locations.append(location)
    return min(locations)


def process_seed_ranges(seeds, maps):
    min_location = float('inf')
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        length = seeds[i+1]
        for seed in range(start, start + length):
            soil = find_destination(seed, maps["seed-to-soil"])
            fertilizer = find_destination(soil, maps["soil-to-fertilizer"])
            water = find_destination(fertilizer, maps["fertilizer-to-water"])
            light = find_destination(water, maps["water-to-light"])
            temperature = find_destination(light, maps["light-to-temperature"])
            humidity = find_destination(temperature, maps["temperature-to-humidity"])
            location = find_destination(humidity, maps["humidity-to-location"])
            min_location = min(min_location, location)
    return min_location


def part2(data):
    """Solve part 2."""
    seeds, maps = data
    return process_seed_ranges(seeds, maps)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    config = configparser.ConfigParser()
    config.read("config.ini")
    day = config.getint("DEFAULT", "day")
    year = config.getint("DEFAULT", "year")
    if Part1:
        solution1 = part1(data)
        submit(solution1, part="a", day=day, year=year)
    else:
        solution2 = part2(data)
        submit(solution2, part="b", day=day, year=year)



if __name__ == "__main__":

    path = "aoc_2023_day_5.txt"
    solve(path)