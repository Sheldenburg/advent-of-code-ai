import os
import re
from dotenv import load_dotenv
from openai import OpenAI
from aocd import get_data
from prompt import SYSTEM, PART1_PROMPT, PART2_PROMPT
import google.generativeai as genai

load_dotenv()

AI_PROVIDER = "google"


def extract_python_code(response_text):
    """Extract the content within the '''python code block."""
    match = re.search(r"```python(.*?)```", response_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def download_aoc_questions(year, day):
    # Get the data for the specified year and day
    data = get_data(year=year, day=day)

    # Save the data to a file
    with open(f"aoc_{year}_day_{day}.txt", "w") as file:
        file.write(data)

    print(f"Question for year {year}, day {day} downloaded successfully.")


def get_genai_response_part1(year: int, day: int):
    # template_path = "/path/to/your/template.py"
    with open("template.py", "r") as file:
        template = file.read()
    with open(f"aoc_{year}_day_{day}.txt", "r") as file:
        input = file.read()

    # system_prompt = SYSTEM.format(
    #     template=template, input_file=input, year=year, day=day
    # )

    system_prompt = SYSTEM.format(input_file=input, year=year, day=day)

    if AI_PROVIDER == "google":
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])

        # Create the model
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 100000,
            "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )

        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        system_prompt,
                    ],
                },
                # {
                #     "role": "model",
                #     "parts": [
                #         template,
                #     ],
                # },
            ]
        )

        response = chat_session.send_message(PART1_PROMPT + template)
        return extract_python_code(response.text)
    if AI_PROVIDER == "openai":
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": PART1_PROMPT},
            ],
        )
        return extract_python_code(completion.choices[0].message.content)


def get_genai_response_part2(year: int, day: int):
    # template_path = "/path/to/your/template.py"
    with open(f"day_{day}_{year}.py", "r") as file:
        template = file.read()
    with open(f"aoc_{year}_day_{day}.txt", "r") as file:
        input = file.read()

    system_prompt = SYSTEM.format(
        template=template, input_file=input, year=year, day=day
    )

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 100000,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[
            # {
            #     "role": "user",
            #     "parts": [
            #         system_prompt,
            #     ],
            # },
            # {
            #     "role": "model",
            #     "parts": [
            #         template,
            #     ],
            # },
            # {
            #     "role": "user",
            #     "parts": [
            #         PART1_PROMPT,
            #     ],
            # },
            # {
            #     "role": "model",
            #     "parts": [
            #         template,
            #     ],
            # },
        ]
    )

    response = chat_session.send_message(PART2_PROMPT + template)
    return extract_python_code(response.text)
