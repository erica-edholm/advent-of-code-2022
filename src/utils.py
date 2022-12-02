import json
import os
from pathlib import Path

import requests

INPUT_URL = "https://adventofcode.com/{0}/day/{1}/input"
ROOT_FOLDER = Path(os.path.abspath(os.curdir))
COOKIE_FILE_PATH = ROOT_FOLDER / "cookie.json"
DATA_DIR = ROOT_FOLDER / "data"


def fetch_input(day):
    input_file_path = DATA_DIR / "day{0}.txt".format(day)
    if not input_file_path.exists():
        download_input(day, input_file_path)
    if input_file_path.exists():
        with open(input_file_path) as file:
            return [line.strip() for line in file]
    else:
        print("No input file found for day{0}".format(day))


def download_input(day, input_file_path):
    url = INPUT_URL.format(2022, day)
    if not COOKIE_FILE_PATH.exists():
        raise ValueError("Could not download input because of missing cookie file")
    with open(COOKIE_FILE_PATH) as cookie_file:
        response = requests.get(url=url, cookies=json.load(cookie_file))
        if response.ok:
            with open(input_file_path, "w") as input_file:
                input_file.writelines(response.text)
            with open(input_file_path, "r") as input_file:
                return [line.strip() for line in input_file]
        if response.status_code == 404:
            return ValueError("Input not available yet for day {0}".format(day))
        raise ValueError("Failed to download input for day {0}.\nStatus code: {1} response: {2} "
                         .format(day, response.status_code, response.text))


def print_solution(part: int, result):
    print(f'Solution part {part}')
    print('********************')
    print(result)
    print('********************')
