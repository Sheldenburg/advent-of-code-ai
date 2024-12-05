import os
import configparser
from utils import (
    download_aoc_questions,
    get_genai_response_part1,
    get_genai_response_part2,
)
from dotenv import load_dotenv

load_dotenv()


def main():
    # Read the day and year from config.ini file

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config.ini"))

    year = config.getint("DEFAULT", "year")
    day = config.getint("DEFAULT", "day")
    filename = f"day_{day}_{year}.py"
    Part1 = os.getenv("Part1", "true").lower() == "true"

    if Part1:
        # Step 2: Download the input file
        download_aoc_questions(year, day)
        # Step 3: Call get_genai_response_part1 to get the answer for part 1
        part1_response = get_genai_response_part1(year, day)

        # Step 4: Save the output of get_genai_response_part1 to a .py file
        with open(filename, "w") as file:
            file.write(part1_response)

    else:
        # Step 5: Call get_genai_response_part2 to get the answer for part 2
        part2_response = get_genai_response_part2(year, day)

        # Save the output of get_genai_response_part2 to a .py file
        with open(filename, "w") as file:
            file.write(part2_response)


if __name__ == "__main__":
    main()
